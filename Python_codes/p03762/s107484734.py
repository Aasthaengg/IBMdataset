from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N,M = inpl()
xx = inpl()
yy = inpl()

l = 0
r = M-1
ySUM = 0
while True:
	if r-l <= 2:
		ySUM += (yy[r]-yy[l])*(r-l)%mod
		break
	else:
		ySUM += (yy[r]-yy[l])*(r-l)%mod
		r,l = r-1,l+1

l = 0
r = N-1
xSUM = 0
while True:
	if r-l <= 2:
		xSUM += (xx[r]-xx[l])*(r-l)%mod
		break
	else:
		xSUM += (xx[r]-xx[l])*(r-l)%mod
		r,l = r-1,l+1

print(xSUM*ySUM%mod)
