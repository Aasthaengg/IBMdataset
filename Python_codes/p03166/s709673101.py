import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5+1)
from functools import lru_cache

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    G[x].append(y)

@lru_cache(maxsize=10**5+1)
def dp(v):
    res = 0
    for w in G[v]:
        res = max(res, dp(w)+1)
    return res

ans = 0
for i in range(N):
    ans = max(ans, dp(i))
print(ans)