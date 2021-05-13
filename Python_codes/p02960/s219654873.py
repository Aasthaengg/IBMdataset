s=input()
n=len(s)
dp=[[0]*13 for _ in range(n)]
if s[-1]=='?':
  for i in range(10):
    dp[n-1][i]=1
else:
  dp[n-1][int(s[-1])]=1
keta=1
mod=10**9+7
for i in range(n-2,-1,-1):
  keta*=10
  keta%=13
  for j in range(13):
    if s[i]!='?':
      dp[i][(int(s[i])*keta+j)%13]+=dp[i+1][j]
      dp[i][(int(s[i])*keta+j)%13]%=mod
      continue
    for k in range(10):
      dp[i][(k*keta+j)%13]+=dp[i+1][j]
      dp[i][(k*keta+j)%13]%=mod
print(dp[0][5])