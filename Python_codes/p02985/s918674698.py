import sys
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, k = tin()
	#s = input()
	tree = [[] for _ in range(n)]
	for _ in range(n-1):
		a, b = tin()
		tree[a-1].append(b-1)
		tree[b-1].append(a-1)
	
	ret = k
	qq = collections.deque()
	qq.append([0, -1])
	opened = set()
	opened.add(0)
	while qq:
		pos, parent = qq.popleft()
		i=0
		for np in tree[pos]:
			if np == parent:
				continue
			qq.append((np, pos))
			
			add = 0
			if parent == -1:
				add = 1
			
			ret *= k-i-2+(add)
			ret %= mod
			i+=1
			#pa((ret, add, parent))
			
	print(ret)
		
	
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)