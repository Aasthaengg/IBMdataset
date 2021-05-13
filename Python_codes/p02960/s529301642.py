s=input()[::-1]
mod=10**9+7
dp=[[0]*13 for i in range(len(s))]
if s[0]=='?':
  for i in range(10):
    dp[0][i]=1
else:
  dp[0][int(s[0])]=1
now=1
for i in range(1,len(s)):
  now=(now*10)%13
  x=s[i]
  if x!='?':
    x=now*int(x)
    for j in range(13):
      dp[i][(j+x)%13]=dp[i-1][j]
  else:
    for j in range(10):
      x=now*j
      for k in range(13):
          dp[i][(k+x)%13]+=dp[i-1][k]
          dp[i][(k+x)%13]=dp[i][(k+x)%13]%mod
print(dp[-1][5]%mod)