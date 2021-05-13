INF=float('inf')

n=int(input())
P=list(map(float,input().split()))#0

dp=[[0 for i in range(n+1)] for j in range(n+1)]
dp[0][0]=1    
for j in range(n+1):
  for i in range(1,n+1):
    if i<j:
      continue
    if j==0:
      dp[i][j]=(1-P[i-1])*dp[i-1][j]
    else:
      dp[i][j]=P[i-1]*(dp[i-1][j-1])+(1-P[i-1])*(dp[i-1][j])

ans=0
for i in range((n+1)//2,n+1):
  ans+=dp[n][i]
    
print(ans)