import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
a = list(map(int, input().split()))
cost = [float("inf"), 2, 5, 5, 4, 5, 6, 3, 7, 6]
mincost = min(cost)

dp = [None] * (n + 1)
def dfs(at):
    if at < 0:
        return -1
    if at == 0:
        return 0
    if dp[at] is not None:
        return dp[at]
    r = max(dfs(at - cost[v]) * 10 + v for v in a)
    dp[at] = r
    return r


print(dfs(n))
