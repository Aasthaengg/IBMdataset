from ctypes import *
import subprocess as sp
from operator import itemgetter
import sys
import os.path

# C++のstd::setのラッパー。こいつを呼び出す。
set_code = r"""
#include <set>

std::set<int> s;

void add(int x) {
    s.insert(x);
}

bool find(int x) {
    return s.find(x) != s.end();
}

void remove(int x) {
    s.erase(x);
}

bool empty() {
	return s.empty();
}

int getMin() {
	return *s.begin();
}
"""

class CppSet:
	# オブジェクトが作られた数
	# オブジェクトごとに共有ライブラリを作成する必要があるので、counterで共有ライブラリにIDを割り振る
	counter = 0

	def __init__(self):
		# 共有ライブラリを作成して、それを呼び出す
		lib_name = './hoge{}.so'.format(CppSet.counter)

		# C++のソースを書き出します
		code_file_name = "tmp.cpp"
		with open(code_file_name, "w") as f:
			f.write(set_code)

		CppSet.counter += 1 

		# 共有ライブラリを作成。-std=c++14とかにすると動かなくなる
		sp.Popen(['g++', '-fPIC', '-shared', '-std=c++11', '-O2', code_file_name, '-o', lib_name]).communicate()

		# Pythonから共有ライブラリを召喚します
		# 召喚方法は https://over80.hatenadiary.jp/entry/20150816/pure_python_inotify を参照
		# 上で書いたコードのgetMinとかの関数が、共有ライブラリではシンボルに変換される(マングリング)らしい
		# なので、シンボルから関数名を得るためにデマングルとかいうやつをやります
		# 最終的にシンボルと関数の対応関係を使って、各関数を召喚します
		# マングリング: https://albel06.hatenablog.com/entry/2016/03/17/180000
		# デマングル: http://0xcc.net/blog/archives/000095.html
		lib = CDLL(lib_name)
		self.add = getattr(lib, "_Z3addi")
		self.find = CFUNCTYPE(c_bool, c_int)(
						("_Z4findi", lib),
						((1, "x"), )
					)
		self.remove = getattr(lib, "_Z6removei")
		self.empty = CFUNCTYPE(c_bool)(
						("_Z5emptyv", lib),
						()
					)

		self.getMin = CFUNCTYPE(c_int)(
						("_Z6getMinv", lib),
						()
					)

def main():
	N, Q = map(int, sys.stdin.readline().split())
	tmp = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
	stx = [(s - x, 1, x) for s, t, x in tmp] + [(t - x, -1, x) for s, t, x in tmp]
	stx.sort()
	
	D = [int(sys.stdin.readline()) for _ in range(Q)] 
	ans = [-1]*Q

	idx = 0
	stx_len = len(stx)
	se = CppSet()
	for i, d in enumerate(D):
		while idx < stx_len:
			t, com, x = stx[idx]
			if t > d:
				break
			if com == 1:
				se.add(x)
			else:
				se.remove(x)
			idx += 1
		ans[i] = (-1 if se.empty() else se.getMin())

	print(*ans, sep='\n')

if __name__ == "__main__":
	main()
