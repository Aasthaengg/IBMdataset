n,m=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]*(n+9)
d=[0,2,5,5,4,5,6,3,7,6]
for i in range(n+1):
  for j in a:
    if dp[i]or i<1:dp[i+d[j]]=max(dp[i+d[j]],dp[i]*10+j)
print(dp[n])