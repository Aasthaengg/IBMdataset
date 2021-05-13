N,M = map(int,input().split())
coins = list(map(int,input().split()))
coins.sort()
dp = [[0] * M for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = i
for j in range(M):
    dp[0][j] = 0
for j in range(1,M):
    for i in range(1,N+1):
        if coins[j] <= i:
            dp[i][j] = min(dp[i-coins[j]][j]+1,dp[i][j-1])     
        else:
            dp[i][j] = dp[i][j-1]
        
print(dp[N][M-1])
