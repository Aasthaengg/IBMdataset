n=int(input())
dp=[[[[0]*4 for i in range(4)] for j in range(4)] for k in range(n)]
mod=10**9+7
for i in range(4):
  for j in range(4):
    for k in range(4):
      if (i,j,k) in ((1,2,3),(1,3,2),(2,1,3)):
        continue
      dp[2][i][j][k]+=1
#t→0 a→1 g→2 c→3
for i in range(1,n):
  for j in range(4):
    for k in range(4):
      for l in range(4):
        for m in range(4):
          if (k,l,m) in ((1,2,3),(2,1,3),(1,3,2)):
            continue
          if (j,l,m)==(1,2,3) or (j,k,m)==(1,2,3):
            continue
          dp[i][k][l][m]+=dp[i-1][j][k][l]
          dp[i][k][l][m]%=mod
ans=0
#print(dp)
for i in range(4):
  for j in range(4):
    for k in range(4):
      ans+=dp[n-1][i][j][k]
      ans%=mod
print(ans)