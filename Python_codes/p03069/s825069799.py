n=int(input())
s=input()
dp=[0]*(n+1)

for i in range(1,n+1):
  if s[i-1]==".":
    cnt=0
  else:
    cnt=1
  dp[i]=dp[i-1]+cnt
ans=n
for i in range(n+1):
  ans=min(ans,dp[i]+(n-i)-(dp[n]-dp[i]))
print(ans)