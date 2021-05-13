N = input()[::-1]
l = len(N)

n0 = int(N[0])
dp = [[0, 0] for i in range(l)]
dp[0] = [n0, 11-n0]

for i, n in enumerate(N[1:], 1):
  n = int(n)
  dp[i][0] = min(dp[i-1][0]+n, dp[i-1][1]+n)
  dp[i][1] = min(dp[i-1][0]+1+(10-n), dp[i-1][1]+(9-n))


print(min(dp[-1]))