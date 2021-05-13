from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m,l = inpl()
d = [[INF]*n for _ in range(n)]
for _ in range(m):
    a,b,c = inpl()
    d[a-1][b-1] = c
    d[b-1][a-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])
e = [[INF]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if d[i][j] <= l:
            e[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            e[i][j] = min(e[i][j], e[i][k]+e[k][j])
q = inp()
for _ in range(q):
    a,b = inpl()
    ans = e[a-1][b-1]
    print(-1 if ans == INF else ans-1)
