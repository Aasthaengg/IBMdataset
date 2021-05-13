from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,pprint,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,m,r = inpl()
x = inpl()
g = [[INF] *n for i in range(n)]
for i in range(m):
    a,b,c = inpl()
    g[a-1][b-1] = c
    g[b-1][a-1] = c
for i in range(n):
    g[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][k]+g[k][j], g[i][j])

res = INF
for flag in itertools.permutations(range(r)):
    cnt = 0
    for i in range(r-1):
        cnt += g[x[flag[i]]-1][x[flag[i+1]]-1]
    res = min(res, cnt)
print(res)