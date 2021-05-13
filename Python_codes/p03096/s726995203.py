from collections import defaultdict
N = int(input())
MOD = 10**9+7
dp = [0]*(N+1)
dp[0] = 1
dic = defaultdict(int)
p = -1
for i in range(N):
  c = int(input())
  if c==p:
    dp[i+1] = dp[i]
    continue
  dic[c] += dp[i]
  dp[i+1] = dic[c]%MOD
  p = c
#  print(dp)

print(dp[-1]%MOD)