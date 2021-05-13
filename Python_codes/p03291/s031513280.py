s=input()
n=len(s)
dp=[4*[0]for i in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
  for j in range(4):
    dp[i][j]+=dp[i-1][j]*((s[i-1]=="?")*2+1)
  if s[i-1] in "A?":dp[i][1]+=dp[i-1][0]
  if s[i-1] in "B?":dp[i][2]+=dp[i-1][1]
  if s[i-1] in "C?":dp[i][3]+=dp[i-1][2]
  for j in range(4):dp[i][j]%=10**9+7
#for i in range(n+1):print(dp[i],(" "+s)[i])
print(dp[-1][-1])