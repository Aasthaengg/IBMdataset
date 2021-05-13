n,m=map(int,input().split())
c=sorted(list(map(int,input().split())))
dp=[10**18]*(n+1)
for i in c:
  if i>n:break
  dp[i]=1
  for j in range(i+1,n+1):
    dp[j]=min(dp[j],dp[j-i]+1)
print(dp[n])
