n,k=map(int,input().split())

dp=[[0 for _ in range(n+1)] for _ in range(k+1)]

for i in range(n+1):
  for j in range(k+1):
    if i>1 and j>0:
      dp[j][i]=(j-1)*dp[j][i-1]
    elif i==1 and j>0:
      dp[j][i]=j
    else:
      dp[j][i]=0

print(dp[k][n])