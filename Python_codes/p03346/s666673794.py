n=int(input())
p=[int(input()) for i in range(n)]
dp=[0]*n
ans=0
for i in range(n):
  if p[i]!=1:
    dp[p[i]-1]=dp[p[i]-2]+1
  else:
    dp[0]=1
print(n-max(dp))