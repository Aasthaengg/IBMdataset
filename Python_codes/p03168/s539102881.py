N = int(input()) # number of coins
tmp = [float(i) for i in input().split()]
dp = [0 for i in range(N+1)] # 0 - N heads
dp[0] = 1
# initialize
for i in range(N):
  k = tmp[i]
  # when the very first coin comes we need to verify update format
  # 1 head or 1 tails
  # j is the number of heads which goes from 0 - N
  for j in range(i+1, -1, -1):
    dp[j] = dp[j-1] * k + dp[j] * (1-k)
ans = 0
for i in range(N+1):
  tails = N-i
  if tails < i:
    ans += dp[i]
print("%s" % ans)