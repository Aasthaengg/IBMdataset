n=int(input())
a=list(map(int,input().split()))
b=[(a[i],i)for i in range(n)]
b.sort(reverse=1)
dp=[(n+1)*[0]for _ in range(n+1)]
for i in range(1,n+1):
  p,j=b[i-1]
  if j<i-1:break
  dp[i][0]+=dp[i-1][0]+p*(j-(i-1))
for i in range(1,n+1):
  p,j=b[i-1]
  if j>(n-i):break
  dp[0][i]+=dp[0][i-1]+p*((n-i)-j)
for i in range(1,n):
  for j in range(1,n):
    if i+j>n:break
    p,k=b[i+j-1]
    if (i-1)<=k:
      dp[i][j]=max(dp[i][j],dp[i-1][j]+p*(k-(i-1)))
    if k<=(n-j):
      dp[i][j]=max(dp[i][j],dp[i][j-1]+p*((n-j)-k))
ans=0
for i in range(n+1):ans=max(ans,dp[i][n-i])
print(ans)