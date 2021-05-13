H, W, K = map(int,input().split())
dp = [[0]*W for _ in range(H+1)]
dp[0][0] = 1

ck = [0]*9
ck[0] = 1
for i in range(1,9):
  for j in range(2**(i-1)):
    for k in range(i-1):
      if (j>>k)&(j>>(k+1))==True:
        break
    else:
      ck[i] += 1

mod = 10**9+7
for i in range(1,H+1):
  for j in range(W):
    if (j == 0)&(j == W-1):
      dp[i][j] = dp[i-1][j]*(ck[j]*ck[W-1-j])
    elif j == 0:
      dp[i][j] = dp[i-1][j+1]*(ck[j]*ck[W-j-2])+dp[i-1][j]*(ck[j]*ck[W-1-j])
    elif j == W-1:
      dp[i][j] = dp[i-1][j]*(ck[j]*ck[W-1-j])+dp[i-1][j-1]*(ck[j-1]*ck[W-j-1])
    else:
      dp[i][j] = dp[i-1][j+1]*(ck[j]*ck[W-j-2])+dp[i-1][j]*(ck[j]*ck[W-1-j])+dp[i-1][j-1]*(ck[j-1]*ck[W-j-1])

print(dp[H][K-1]%mod)