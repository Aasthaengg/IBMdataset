n,s = map(int,input().split())
a = tuple(map(int,input().split()))
MOD = 998244353

# dp[i][j]:Aをi番目まで見たときに、和がjとなるTの個数。
dp = [[0 for _ in range(s+1)] for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
  ai = a[i]
  for j in range(s+1):
    dp[i+1][j] += 2*dp[i][j] #aiを選ぶか選ばないかの2通りある。
    dp[i+1][j] %= MOD
    if j+ai <= s:
      dp[i+1][j+ai] += dp[i][j]
      dp[i+1][j+ai] %= MOD
print(dp[n][s])
#print(dp)