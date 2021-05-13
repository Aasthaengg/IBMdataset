import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
mod = 998244353
N,S = map(int,readline().split())
A = list(map(int,readline().split()))
dp = [[0 for _ in range(S+1)] for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
  for j in range(S+1):
    dp[i+1][j] += 2*dp[i][j]
    dp[i+1][j] %= mod
    if j + A[i] <=S:
      dp[i+1][j+A[i]] += dp[i][j]
      dp[i+1][j+A[i]] %= mod
print(dp[N][S]%mod)