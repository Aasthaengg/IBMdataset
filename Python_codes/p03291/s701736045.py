s=input()
l=len(s)
dp=[4*[0]for _ in range(l+1)]
dp[0][0]=1
for i in range(1,l+1):
  si=s[i-1]
  for j in range(4):dp[i][j]=dp[i-1][j]*((si=="?")*2+1)
  if si=="A":dp[i][1]+=dp[i-1][0]
  if si=="B":dp[i][2]+=dp[i-1][1]
  if si=="C":dp[i][3]+=dp[i-1][2]
  if si=="?":
    dp[i][1]+=dp[i-1][0]
    dp[i][2]+=dp[i-1][1]
    dp[i][3]+=dp[i-1][2]
  for j in range(4):dp[i][j]%=10**9+7
print(dp[-1][-1])