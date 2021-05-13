n = int(input())
p = [0] + list(map(float, input().split()))
q = [1 - p[i] for i in range(n + 1)]
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(n + 1):
        dp[i][j] = dp[i - 1][j] * q[i]
        if not j == 0:
            dp[i][j] += dp[i - 1][j - 1] * p[i]
ans = 0
for i in range((n + 1) // 2):
    ans += dp[n][n - i]
print(ans)