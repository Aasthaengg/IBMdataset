n=int(input())
a=list(map(float,input().split()))
ans=0

dp=[[0]*(n+1) for i in range(n+1)]
dp[0][0]=1

for i in range(n):
  for j in range(i+1):
    dp[i+1][j+1]=dp[i][j]*a[i]+dp[i][j+1]*(1-a[i])
    dp[i+1][j]=dp[i][j]*(1-a[i])+dp[i][j-1]*(a[i])
  
  
for i in range(n//2+1,n+1):
  ans+=dp[-1][i]
  
  
print(ans)