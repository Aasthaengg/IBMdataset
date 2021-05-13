N = int(input())
p = [0] + list(map(float, input().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(N + 1):
        dp[i][j] = dp[i - 1][j - 1] * p[i] + dp[i - 1][j] * (1 - p[i])

print(sum(dp[N][i] for i in range(N // 2 + 1, N + 1)))