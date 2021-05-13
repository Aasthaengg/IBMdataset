n = int(input())
arr = list(map(float, input().split()))

dp = [[0.0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1.0

for i in range(n):
    for j in range(i + 1):
        dp[i + 1][j + 1] += dp[i][j] * arr[i]
        dp[i + 1][j] += dp[i][j] * (1 - arr[i])

dp = dp[-1]

print(sum(dp[-(n + 1) // 2:]))