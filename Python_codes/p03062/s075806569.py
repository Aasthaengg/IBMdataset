
N = int(input())
X = list(map(int, input().split()))

dp = [[0, 0] for _ in range(N + 1)]
dp[0][1] = -10**9
for i in range(N):
    dp[i + 1][0] = max(dp[i][0] + X[i], dp[i][1] - X[i])
    dp[i + 1][1] = max(dp[i][0] - X[i], dp[i][1] + X[i])

print(dp[-1][0])
