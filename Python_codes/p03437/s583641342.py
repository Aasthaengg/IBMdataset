from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

X,Y = inpl()
if X%Y == 0:
	print(-1)
else:
	print(X*(Y+1))
