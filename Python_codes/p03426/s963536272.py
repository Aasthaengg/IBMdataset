from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

h,w,d = inpl()
n = h*w
di = dict()
for i in range(h):
    x = inpl()
    for j in range(w):
        di[x[j]-1] = (i,j)
a = []
for i in range(d):
    tmp = [0]
    for j in range(i,n,d):
        if j == i:
            px,py = di[j]
            continue
        nx,ny = di[j]
        tmp.append(abs(nx-px)+abs(ny-py))
        px,py = nx,ny
    a.append(list(itertools.accumulate(tmp)))

q = inp()
for _ in range(q):
    l,r = inpl()
    l,r = l-1, r-1
    now = l%d
    print(a[now][(r-now)//d] - a[now][(l-now)//d])