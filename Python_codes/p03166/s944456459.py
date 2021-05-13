import sys
sys.setrecursionlimit(10 ** 7)


def input():
    return sys.stdin.readline().strip()


def dfs(v):
    if dp[v] >= 0:
        return dp[v]
    res = 0
    for nv in g[v]:
        res = max(res, dfs(nv) + 1)
    dp[v] = res
    return res


n, m = map(int, input().split())
g = [[] for i in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x - 1].append(y - 1)

dp = [-1] * n
for v in range(n):
    dp[v] = max(dp[v], dfs(v))
print(max(dp))
