INFTY = 10**4
N,Ma,Mb = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
dp = [[[INFTY for _ in range(401)] for _ in range(401)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(1,N+1):
    for j in range(401):
        for k in range(401):
            dp[i][j][k] = dp[i-1][j][k]
            a = A[i-1][0]
            b = A[i-1][1]
            c = A[i-1][2]
            if j>=a and k>=b:
                dp[i][j][k] = min(dp[i][j][k],dp[i-1][j-a][k-b]+c)
cmin = INFTY
for j in range(1,401):
    for k in range(1,401):
        if j*Mb==k*Ma:
            cmin = min(cmin,dp[N][j][k])
if cmin>=INFTY:
    print(-1)
else:
    print(cmin)