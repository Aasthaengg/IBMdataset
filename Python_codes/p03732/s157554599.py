n,w = map(int,input().split())
l =[list(map(int,input().split())) for i in range(n)]

dp = [[[0]*(3*n+1) for i in range(n+1)] for j in range(n+1)]
s = l[0][0]

for i in range(n):
    dt = l[i][0]-s
    for j in range(n):
        for k in range(3*n+1):
            if k -dt >= 0:
                dp[i+1][j+1][k] = max(dp[i][j+1][k],dp[i][j][k-dt]+l[i][1])
            else:
                dp[i+1][j+1][k] = dp[i][j+1][k]

ans = 0
for i in range(1,n+1):
    for j in range(3*n+1):
        if i*s+j <= w:
            ans = max(ans,dp[-1][i][j])
print(ans)