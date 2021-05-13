INF=float('inf')

n=int(input())
P=list(map(float,input().split()))#0

dp=[[0 for i in range(n+1)] for j in range(n+1)]

for i in range(n+1):
  if i==0:
    dp[0][0]=1
  else:
    dp[i][0]=(1-P[i-1])*dp[i-1][0]

    
for j in range(1,n+1):
  for i in range(1,n+1):
    if i<j:
      continue
    dp[i][j]=P[i-1]*(dp[i-1][j-1])+(1-P[i-1])*(dp[i-1][j])

ans=0
for i in range(1,n+1):
  if i>=(n+1)//2:
    ans+=dp[n][i]
    
print(ans)