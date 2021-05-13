N,A,B=map(int,input().split())
inf=float("inf")
dp=[[inf]*401 for _ in range(401)]
dp[0][0]=0
for i in range(N):
    a,b,c=map(int,input().split())
    for j in range(-1,-402,-1):
        for k in range(-1,-402,-1):
            if dp[j][k]!=inf:
                dp[j+a][k+b]=min(dp[j+a][k+b],dp[j][k]+c)
ans=inf
for i in range(1,401):
    for j in range(1,401):
        if i/j==A/B:
            ans=min(ans,dp[i][j])
if ans==inf:
    ans=-1
print(ans)