h,n=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
dp=[[10**9+1]*(h+1) for i in range(n+1)]
for i in dp:
  i[0]=0

for i in range(n):
  for j in range(h+1):
    if j-ab[i][0]>=0:
      dp[i+1][j]=min(dp[i][j],dp[i+1][j-ab[i][0]]+ab[i][1],(j//ab[i][0]+1)*ab[i][1])
    else:
      dp[i+1][j]=min(dp[i][j],ab[i][1])
print(dp[-1][h])