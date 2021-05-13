num=[0,2,5,5,4,5,6,3,7,6]
n,m=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]*(n+17)
for i in range(n+1):
  for j in a:
    if i==0 or dp[i]>0:dp[i+num[j]]=max(dp[i+num[j]],dp[i]*10+j)
print(dp[n])