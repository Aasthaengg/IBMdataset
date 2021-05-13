import sys
input = sys.stdin.readline
n, m = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
for _ in range(m):
    x, y = [int(x) for x in input().split()]
    g[x - 1].append(y - 1)
from functools import lru_cache
sys.setrecursionlimit(10**7)
@lru_cache(maxsize=None)
def dp(v):
    res = 0
    for u in g[v]:
        res = max(res, dp(u) + 1)
    return res
ans = -1
for i in range(n):
    ans = max(ans, dp(i))
print(ans)


