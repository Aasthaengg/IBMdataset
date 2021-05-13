n=int(input())
p = list(map(float,input().split()))
dp = [[0 for _ in range(n+1)] for __ in range(n+1)]
dp[0][0] = 1
for i in range(n+1):
    for j in range(n+1):
        cnt = i + j
        if cnt == 0 or cnt > n:
            continue
        if j == 0:
            dp[i][j] = dp[i-1][0] * p[cnt-1]
        elif i == 0:
            dp[i][j] = dp[i][j-1] * (1 - p[cnt-1])
        else:
            dp[i][j] = dp[i-1][j]*p[cnt-1] + dp[i][j-1]*(1-p[cnt-1])
        
ans = 0
for i in range((n+1)//2, n+1):
    ans += dp[i][n-i]
print(ans)