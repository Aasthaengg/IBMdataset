from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m,r = inpl()
rr = inpl()
g = [[INF]*n for _ in range(n)]
for i in range(n):
    g[i][i] = 0
for i in range(m):
    a,b,c = inpl()
    a,b = a-1,b-1
    g[a][b] = c
    g[b][a] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], g[i][k]+g[k][j])
res = INF
for root in itertools.permutations(range(r)):
    cnt = 0
    for i in range(r-1):
        a,b = rr[root[i]], rr[root[i+1]]
        a,b = a-1, b-1
        cnt += g[a][b]
    res = min(res, cnt)
print(res)