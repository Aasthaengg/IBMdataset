s = str(input());MOD = pow(10,9)+7
n = len(s)
dp = [[0,0,0,0]  for _ in range(n+1)]
#i番目まで見て、(x,a,ab,abc)で終わる個数。
dp[0][0] = 1
for i in range(n):
  if s[i] == "A":
    dp[i+1][0] = dp[i][0]
    dp[i+1][1] = dp[i][0]+dp[i][1]
    dp[i+1][2] = dp[i][2]
    dp[i+1][3] = dp[i][3]
  if s[i] == "B":
    dp[i+1][0] = dp[i][0]
    dp[i+1][1] = dp[i][1]
    dp[i+1][2] = dp[i][2]+dp[i][1]
    dp[i+1][3] = dp[i][3]
  if s[i] == "C":
    dp[i+1][0] = dp[i][0]
    dp[i+1][1] = dp[i][1]
    dp[i+1][2] = dp[i][2]
    dp[i+1][3] = dp[i][3]+dp[i][2]
  if s[i] == "?":
    dp[i+1][0] = dp[i][0]*3
    dp[i+1][1] = dp[i][1]*3+dp[i][0]
    dp[i+1][2] = dp[i][2]*3+dp[i][1]
    dp[i+1][3] = dp[i][3]*3+dp[i][2]
  for j in range(4):
    dp[i+1][j] %= MOD
    
ans = dp[n][3]
#print(dp)
print(ans)