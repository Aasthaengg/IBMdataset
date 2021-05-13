from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m,q = inpl()
g = [[0]*n for _ in range(n)]
gg = [[0]*n for _ in range(n)]
for _ in range(m):
    l,r = inpl()
    l,r = l-1, r-1
    g[l][r] += 1
for i in range(n)[::-1]:
    for j in range(n):
        # print(i)
        if i == n-1:
            gg[i][j] += g[i][j]
            continue
        gg[i][j] += g[i][j] + gg[i+1][j]
# print(gg)
for i in range(n):
    for j in range(n-1):
        gg[i][j+1] += gg[i][j]

# pprint.pprint(gg)
for _ in range(q):
    a,b = inpl()
    a,b = a-1,b-1
    print(gg[a][b])