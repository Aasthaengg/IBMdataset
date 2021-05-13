n=int(input())
mod=10**9+7
dp=[[[[0]*4 for i in range(4)] for j in range(4)] for k in range(n+1)]
for i in range(4):
  for j in range(4):
    for k in range(4):
      dp[3][i][j][k]=1
dp[3][0][2][1]=0
dp[3][0][1][2]=0
dp[3][2][0][1]=0
for i in range(4,n+1):
  for j in range(4):
    for k in range(4):
      for l in range(4):
        for m in range(4):
          dp[i][j][k][l]=(dp[i][j][k][l]+dp[i-1][m][j][k])%mod
          if m==0 and k==2 and l==1:
            dp[i][j][k][l]=0
          if m==0 and j==2 and l==1:
            dp[i][j][k][l]=0
  dp[i][0][2][1]=0
  dp[i][0][1][2]=0
  dp[i][2][0][1]=0
ans=0
for i in range(4):
  for j in range(4):
    for k in range(4):
      ans=(ans+dp[n][i][j][k])%mod
print(ans)