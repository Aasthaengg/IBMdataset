MOD=10**9+7
n=int(input())
dp=[]
for i in range(n+1):
  dp.append([])
  for j in range(4):
    dp[-1].append([])
    for k in range(4):
      dp[-1][-1].append([])
      for l in range(4):
        dp[-1][-1][-1].append(0)
for i in range(4):
  for j in range(4):
    for k in range(4):
      dp[3][i][j][k]=1
dp[3][0][1][2]=0
dp[3][0][2][1]=0
dp[3][1][0][2]=0
for i in range(3,n):
  for j in range(4):
    for k in range(4):
      for l in range(4):
        dp[i+1][k][l][0]=(dp[i+1][k][l][0]+dp[i][j][k][l])%MOD
        dp[i+1][k][l][1]=(dp[i][j][k][l]+dp[i+1][k][l][1])%MOD
        dp[i+1][k][l][3]=(dp[i][j][k][l]+dp[i+1][k][l][3])%MOD
        if not((j==0 and k==1) or (j==0 and l==1)):
          dp[i+1][k][l][2]=(dp[i+1][k][l][2]+dp[i][j][k][l])%MOD
  dp[i+1][0][1][2]=0
  dp[i+1][0][2][1]=0
  dp[i+1][1][0][2]=0
ans=0
for i in range(4):
  for j in range(4):
    for k in range(4):
      ans=(ans+dp[n][i][j][k])%MOD
print(ans)