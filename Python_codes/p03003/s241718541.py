MOD = pow(10, 9) + 7

n, m = map(int, input().split())
slist = list(map(int, input().split()))
tlist = list(map(int, input().split()))

dp = [[1 for _ in range(n+1)] for _ in range(m+1)]
for i, s in enumerate(slist):
  for j, t in enumerate(tlist):
    if s != t:
      dp[j+1][i+1] = ((dp[j+1][i] + dp[j][i+1]) % MOD - dp[j][i]) % MOD
    else:
      #if slist[i] == t and tlist[j] == s:
        dp[j+1][i+1] = (dp[j+1][i] + dp[j][i+1]) % MOD
      #else:
      #  dp[j+1][i+1] = ((dp[j+1][i] + dp[j][i+1]) % MOD - dp[j][i]) % MOD

print(dp[-1][-1])
