import sys
from io import StringIO
import unittest
import os
from collections import deque
import collections

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    n, x, y = map(int, input().split())

    ans = []

    for i in range(1, n + 1):

        que = deque()
        que.append(i)
        work_ans = [9999 for i in range(n + 1)]
        work_ans[i] = 0

        while len(que) is not 0:

            now = que.pop()
            # 移動する方向を設定
            target = []
            if now > 1:
                target.append(now - 1)
            if now < n:
                target.append(now + 1)
            if now == x:
                target.append(y)
            if now == y:
                target.append(x)

            for j in target:
                # 既に最適解が設定されている場合は処理をしない
                if work_ans[j] < work_ans[now] + 1:
                    continue
                # 最適解の設定と、キュー追加を実施。
                work_ans[j] = work_ans[now] + 1
                que.appendleft(j)

        ans += work_ans

    # Counter()で、各数字の個数を数える。
    counter = collections.Counter(ans)

    # 各距離の個数を出力(全網羅しているので、「÷2」して集計時の重複を排除する。)
    for i in range(1, n):
        print(counter.get(i, 0)//2)


# テストクラス
class TestClass(unittest.TestCase):
    def assertIO(self, assert_input, output):
        stdout, sat_in = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(assert_input)
        resolve(sys._getframe().f_back.f_code.co_name)
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, sat_in
        self.assertEqual(out, output)

    def test_input_1(self):
        test_input = """5 2 4"""
        output = """5
4
1
0"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """3 1 3"""
        output = """3
0"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """7 3 7"""
        output = """7
8
4
2
0
0"""
        self.assertIO(test_input, output)

    def test_input_4(self):
        test_input = """10 4 8"""
        output = """10
12
10
8
4
1
0
0
0"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def tes_t_1original_1(self):
        test_input = """データ"""
        output = """データ"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
