import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    G[x].append(y)

memo = [-1]*n
def dp(v):
    if memo[v] != -1:
        return memo[v]
    res = 0
    for nv in G[v]:
        res = max(res, dp(nv) + 1)
    
    memo[v] = res
    return res

ans = 0
for v in range(n):
    ans = max(ans, dp(v))
print(ans)