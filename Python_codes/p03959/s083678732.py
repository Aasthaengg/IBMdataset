from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())

N = int(input())
tt = inpl()
aa = inpl()
hh = [[0,0] for i in range(N)]

bt = 0
for i in range(N):
	t = tt[i]
	if t != bt:
		hh[i] = [t,t]
	else:
		hh[i] = [1,t]
	bt = t

ba = 0
for i in reversed(range(N)):
	a = aa[i]
	MIN,MAX = hh[i]
	if a != ba:
		if MIN <= a <= MAX:
			hh[i] = [a,a]
		else:
			print(0)
			sys.exit()
	else:
		hh[i] = [max(1,MIN),min(a,MAX)]

	ba = a

ans = 1
for azu,nyan in hh:
	ans *= (nyan-azu+1)
	ans %= mod

print(ans)
