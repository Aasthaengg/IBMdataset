n = int(input())
a = list(map(float, input().split()))

# dp = [[None] * 1501 for i in range(3000)]
# def dfs(i=0, at=(n + 1) // 2):
#     if i == n:
#         return int(at <= 0)
#     at = max(at, 0)
#     if dp[i][at] is not None:
#         return dp[i][at]
#
#     r = dfs(i + 1, at - 1) * a[i] + dfs(i + 1, at) * (1 - a[i])
#     dp[i][at] = r
#     return r
# print(dfs())

dp = [[0] * 1501 for i in range(3000)]
dp[n][0] = 1
for i in reversed(range(n)):
    for at in reversed(range((n + 1) // 2 + 1)):
        r = dp[i + 1][max(0, at - 1)] * a[i] + dp[i + 1][at] * (1 - a[i])
        dp[i][at] = r

print(dp[0][(n + 1) // 2])

