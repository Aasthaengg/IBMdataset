H, W, K = map(int, input().split())
MOD = 10**9+7
dp = [[0]*W for i in range(H+1)]
dp[0][0] = 1
ls = []
for h in range(2**(W-1)):
  log = ''
  flag = True
  for x in range(W-1):
    if h%2==1 and flag:
      log += '1'
      flag = False
    else:
      log += '0'
      flag = True
    h >>= 1
  ls += [log]
if W==1:
  ls = ['0']
ls = set(ls)
for i in range(H):
  for j in range(W):
#    print(dp[-1], j)
    for log in ls:
      if j==0:
        if log[j]=='1':
          dp[i+1][j+1] += dp[i][j]%MOD
        else:
          dp[i+1][j] += dp[i][j]%MOD
      elif j==W-1:
        if log[j-1]=='1':
          dp[i+1][j-1] += dp[i][j]%MOD
        else:
          dp[i+1][j] += dp[i][j]%MOD
      else:
        if log[j-1]=='1':
          dp[i+1][j-1] += dp[i][j]%MOD
        elif log[j]=='1':
          dp[i+1][j+1] += dp[i][j]%MOD
        else:
          dp[i+1][j] += dp[i][j]%MOD
print(dp[-1][K-1]%MOD)