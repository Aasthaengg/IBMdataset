n=int(input())
s=[list(input()) for i in range(2)]
mod=10**9+7
idx=0
dp=[0]*n
if s[0][0]==s[1][0]:
  dp[0]=3
  idx+=1
else:
  dp[0]=6
  dp[1]=dp[0]
  idx+=2
while idx<n:
  if s[0][idx]==s[1][idx] and s[0][idx-1]!=s[1][idx-1]:
    dp[idx]=dp[idx-1]
    idx+=1
  elif s[0][idx]!=s[1][idx] and s[0][idx-1]==s[1][idx-1]:
    dp[idx+1]=dp[idx]=(dp[idx-1]*2)%mod
    idx+=2
  elif s[0][idx]==s[1][idx] and s[0][idx-1]==s[1][idx-1]:
    dp[idx]=(dp[idx-1]*2)%mod
    idx+=1
  else:
    dp[idx+1]=dp[idx]=(dp[idx-1]*3)%mod
    idx+=2
print(dp[n-1])