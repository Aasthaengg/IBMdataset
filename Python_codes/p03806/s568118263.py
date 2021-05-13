n,ma,mb=map(int,input().split())
dp=[[[4001]*401 for _ in range(401)] for j in range(n+1)]
dp[0][0][0]=0
a=[0]*n; b=[0]*n; c=[0]*n
for i in range(n):
    a[i],b[i],c[i]=map(int,input().split())

for i in range(n):
    for j in range(401):
        for k in range(401):
            if dp[i][j][k]==4001:
                continue
            dp[i+1][j][k]=min(dp[i+1][j][k], dp[i][j][k])
            dp[i+1][j+a[i]][k+b[i]]=min(dp[i+1][j+a[i]][k+b[i]],dp[i][j][k]+c[i])

ans=4001
for i in range(1,401):
    for j in range(1,401):
        if i*mb==j*ma:
            ans=min(ans,dp[n][i][j])

print(ans if ans!=4001 else -1)
