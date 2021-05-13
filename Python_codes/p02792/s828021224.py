n = int(input())
dp = [[0]*10 for i in range(10)]
su = 0
for i in range(1,n+1):
  a,b = str(i)[0],str(i)[-1]
  dp[int(a)-1][int(b)-1] += 1
for i in range(10):
  for j in range(10):
    su += dp[i][j]*dp[j][i]
print(su)