N, K = map(int, input().split())
*A, = map(int, input().split())

dp = [[-1]*(K + 1) for _ in range(N + 1)]
for j in range(K + 1):
    dp[0][j] = 0

for i in range(N):
    for j in range(K + 1):
        if j >= 1:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - 1] + A[i])
        else:
            dp[i + 1][j] = dp[i][j]
            
print(dp[N][K])