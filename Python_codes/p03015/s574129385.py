# E - Sum Equals Xor
l = input()
n =len(l)

# a+b=a^b+a&b*2なので、a+b=a^bということは、a&b=0
# a&b=0となるようにa,bの各桁を決めていく。
# dp[i][j]:上からi桁目みたときの、組(a,b)の数。
#          j=0:i桁目までのa+bがlと一致。j=1:i桁目までのa+bがl未満であることが確定。

MOD = 10**9+7
dp = [[0 for _ in range(2)] for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
  #a+b=0のパターン(aの桁もbの桁も0)
  if l[i] == '0':
    dp[i+1][0] += dp[i][0]
    dp[i+1][1] += dp[i][1]
  else:
    dp[i+1][1] += dp[i][0]+dp[i][1]
  #a+b=1のパターン(aの桁とbの桁のどちらかが1でどちらかが0。->2パターンある。)
  if l[i] == '0':
    dp[i+1][1] += dp[i][1]*2
  else:
    dp[i+1][0] += dp[i][0]*2
    dp[i+1][1] += dp[i][1]*2
  dp[i+1][0] %= MOD
  dp[i+1][1] %= MOD

print((dp[n][0]+dp[n][1])%MOD)