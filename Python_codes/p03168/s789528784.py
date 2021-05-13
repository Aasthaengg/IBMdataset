n = int(input())
p = list(map(float,input().split()))
dp = [[0] * (n+1) for i in range(n+1)]
dp[0][0] = 1
for i in range(1,n+1):
    for j in range(i+1):
        if j > 0:
            dp[i][j] = dp[i-1][j]*(1-p[i-1])+dp[i-1][j-1]*p[i-1]
        else:
            dp[i][j] = dp[i-1][j]*(1-p[i-1])
ans = 0
for i in range(n//2+1,n+1):
    ans += dp[n][i]
print(ans)