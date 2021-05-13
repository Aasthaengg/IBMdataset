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

n,q = inpl()
g = [[]for i in range(n)]
c = [0 for i in range(n)]
seen = [False] * n
for i in range(n-1):
    a,b = inpl()
    g[a-1].append(b-1)
    g[b-1].append(a-1)
for i in range(q):
    a,b = inpl()
    c[a-1] += b
def dfs(node):
    for v in g[node]:
        if seen[v]:
            continue
        c[v] += c[node]
        seen[v] = True
        dfs(v) 
seen[0] = True
dfs(0)
print(*c)
