MOD = 998244353
N, K = map(int, input().split())
LR = [tuple(map(int, input().split())) for i in range(K)]
 
dp = [0] * (N+1)
dp[1] = 1    #ok
for i in range(1, N):
  dp[i] += dp[i-1]   #as min k = 1, so carry this on to the next
  dp[i] %= MOD
  for l, r in LR:
    ll = i + l
    rr = i + r
    if ll <= N:
      dp[ll] += dp[i]    #yes ll is accesible
      dp[ll] %= MOD
    if rr < N:
      dp[rr+1] -= dp[i]    #not accessible and will get cancelled out when we take prefix sum
      dp[rr+1] %= MOD
 
print(dp[-1])