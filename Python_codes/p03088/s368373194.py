n = int(input())
mask = 0b111111
mod = 10**9+7
dp = [[0]*4**3 for _ in range(n+1)]
dp[0][63] = 1
for i in range(n):
  for bit in range(4**3):
    for x in range(4):
      nb = bit<<2&63|x
      f = nb == 6 or nb == 9 or nb == 33
      f |= bit&51 == 2 and x == 1
      f |= bit&60 == 8 and x == 1
      if f:
        continue
      dp[i+1][nb] += dp[i][bit]
      dp[i+1][nb] %= mod
print(sum(dp[-1])%mod)