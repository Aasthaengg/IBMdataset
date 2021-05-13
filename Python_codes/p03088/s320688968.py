n = int(input())
mod = 10**9 + 7
dp = [[[[0 for _ in range(n+1)] for _ in range(4)]for _ in range(4)] for _ in range(4)]

for i in range(4):
  for j in range(4):
    for k in range(4):
      if((i == 0 and j == 1 and k == 2) or (i == 0 and j == 2 and k == 1) or (i == 1 and j == 0 and k == 2)):
        pass
      else:
        dp[i][j][k][3] = 1
        
for length in range(3, n):
  for i in range(4):
    for j in range(4):
      for k in range(4):
        if(j == 0 and k == 2):
          dp[j][k][0][length + 1] += (dp[i][j][k][length])%mod
          dp[j][k][2][length + 1] += (dp[i][j][k][length])%mod
          dp[j][k][3][length + 1] += (dp[i][j][k][length])%mod
        elif((i == 0 and k == 1) or (i == 0 and j == 1) or (j == 0 and k == 1) or (j == 1 and k == 0)):
          dp[j][k][0][length + 1] += (dp[i][j][k][length])%mod
          dp[j][k][1][length + 1] += (dp[i][j][k][length])%mod
          dp[j][k][3][length + 1] += (dp[i][j][k][length])%mod
        else:
          dp[j][k][0][length + 1] += (dp[i][j][k][length])%mod
          dp[j][k][1][length + 1] += (dp[i][j][k][length])%mod
          dp[j][k][2][length + 1] += (dp[i][j][k][length])%mod
          dp[j][k][3][length + 1] += (dp[i][j][k][length])%mod
ans = 0
for i in range(4):
  for j in range(4):
    for k in range(4):
      ans += dp[i][j][k][n]
      
print(ans%mod)
          

