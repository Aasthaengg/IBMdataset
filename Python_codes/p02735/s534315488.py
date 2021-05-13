h,w=map(int,input().split())
G=[["#"]*(w+2) for i in range(h+2)]
for i in range(1,h+1):
  G[i]=["#"]+list(input())+["#"]
for i in range(h+2):
  for j in range(w+2):
    if G[i][j]==".":
      G[i][j]=0
    else:
      G[i][j]=1
dp=[[1000]*(w+2) for i in range(h+2)]
dp[1][1]=0
for i in range(1,h+1):
  for j in range(1,w+1):
    if i==1 and j==1:
      continue
    dp[i][j]=min(dp[i-1][j]+(G[i-1][j]+G[i][j])%2,dp[i][j-1]+(G[i][j-1]+G[i][j])%2)
ans=dp[h][w]
if G[1][1]==1:
  ans=ans+1
print((ans+1)//2)