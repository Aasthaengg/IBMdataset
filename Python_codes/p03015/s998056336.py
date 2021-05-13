L = str(input());MOD = pow(10,9)+7
N = len(L) #N桁

dp = [[0]*2 for _ in range(N+1)]
#dp[i+1][j]
#i桁目で和が完全一致ならj=1
#それ以外ならj=0
dp[0][1] = 1

for i in range(N):
  if L[i] == "0":
    dp[i+1][1] = dp[i][1] #j=1で(0,0)
    dp[i+1][0] = dp[i][0]*3%MOD #j=0で何でもよい
  else:
    dp[i+1][1] = dp[i][1]*2%MOD
    dp[i+1][0] = (dp[i][1] + dp[i][0]*3)%MOD 
ans = (dp[N][0] + dp[N][1])%MOD
print(ans)