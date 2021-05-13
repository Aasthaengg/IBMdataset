from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

A,B =inpl()
A -= 1
B -= 1

H,W = 41,100
ans = []

for y in range(H//2+1):
	tmp = []
	if y%2==0:
		tmp = ['.']*W
	else:
		for x in range(W):
			if x%2==1 and y%2==1 and B>0:
				tmp.append('#')
				B -= 1
			else:
				tmp.append('.')
	ans.append(tmp)

for y in range(H//2+1,H):
	tmp = []
	if y%2==1:
		tmp = ['#']*W
	else:
		for x in range(W):
			if x%2==1 and y%2==0 and A>0:
				tmp.append('.')
				A -= 1
			else:
				tmp.append('#')
	ans.append(tmp)

print(H,W)
for a in ans:
	print (''.join(a))
