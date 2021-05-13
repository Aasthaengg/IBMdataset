N=int(input())
INF=10**10
dp=[[-1]*3 for i in range(N)]
for i in range(N):
  abc=list(map(int,input().split()))
  if i==0:
    dp[0][0]=abc[0]
    dp[0][1]=abc[1]
    dp[0][2]=abc[2]
    continue
  for j in range(3):
    for k in range(3):
      if j==k:continue
      dp[i][j]=max(dp[i][j],dp[i-1][k]+abc[j])
print(max(dp[-1]))