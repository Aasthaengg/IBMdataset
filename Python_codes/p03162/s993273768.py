n=int(input())
abc=[[-1,-1,-1,-1]]

for i in range(n):
  a,b,c=map(int,input().split())
  abc.append([-1,a,b,c])
dp=[[0 for i in range(4)] for j in range(n+1)]

for i in range(1,n+1):
  for j in range(1,4):
    for k in range(1,4):
      if j==k:
        continue
      dp[i][k]=max(dp[i][k],dp[i-1][j]+abc[i][k])
ans=max(dp[n])
print(ans)