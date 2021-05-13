N = int(input())
P = list(map(float, input().strip().split()))

dp = [[0 for i in range(N+1)] for i in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    dp[i][0] = (1-P[i-1])*dp[i-1][0]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = P[i-1]*dp[i-1][j-1] + (1-P[i-1])*dp[i-1][j] 

print(sum(dp[N][N//2+1:]))