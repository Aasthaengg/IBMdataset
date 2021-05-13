n,m=map(int,input().split())
dp=[0]*(n+1)
for i in range(m):
  a,b=map(int,input().split())
  dp[a]+=1
  dp[b]+=1
for i in range(1,n+1):
  print(dp[i])
