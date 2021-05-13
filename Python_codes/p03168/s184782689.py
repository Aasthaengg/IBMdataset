N = int(input())
p = list(map(float, input().split()))

dp = [[0.0] * (N + 1) for _ in range(N + 1)]
dp[1][0] = 1 - p[0]
dp[1][1] = p[0]
for i in range(2, N + 1):
    for j in range(N + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] * (1 - p[i - 1])
        else:
            dp[i][j] = dp[i - 1][j] * (1 - p[i - 1]) + dp[i - 1][j - 1] * p[i - 1]
M = N // 2 + 1
ans = 0
for i in range(M, N + 1):
    ans += dp[-1][i]
print(ans)