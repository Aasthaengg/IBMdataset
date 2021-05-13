N,W = map(int,input().split())
item = [list(map(int,input().split())) for i in range(N)]
w = item[0][0]

dp = [[[0 for k in range(3*N+1)] for j in range(N+1)] for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i+1):
        for k in range(3*j+1):
            if item[i-1][0]-w <= k:
                dp[i][j][k] = max(dp[i-1][j-1][k-(item[i-1][0]-w)]+item[i-1][1],dp[i-1][j][k])
            else:
                dp[i][j][k] = dp[i-1][j][k]
                
ans = 0
for j in range(N+1):
    for k in range(3*N+1):
        if j*w+k <= W:
            ans = max(ans,dp[N][j][k])
            
print(ans)