N, Ma, Mb = map(int, input().split())
dp = [[[10**18]*401 for _ in range(401)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    a, b, c = map(int, input().split())
    
    for j in range(401):
        for k in range(401):
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
            
            if j+a<=400 and k+b<=400:
                dp[i+1][j+a][k+b] = min(dp[i+1][j+a][k+b], dp[i][j][k]+c)

ans = 10**18

for i in range(401):
    for j in range(401):
        if i>0 and j>0 and i*Mb==j*Ma:
            ans = min(ans, dp[N][i][j])

if ans==10**18:
    print(-1)
else:
    print(ans)