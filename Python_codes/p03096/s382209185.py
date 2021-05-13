from collections import defaultdict
def solve():
  ans = 0
  N = int(input())
  C = [int(input()) for _ in range(N)]
  d = defaultdict(lambda: -1)
  dp = [1]*N
  d[C[0]] = 0
  mod = 10**9+7
  for i in range(1,N):
    dp[i] = dp[i-1]
    if d[C[i]]>-1 and d[C[i]]!=i-1:
      dp[i] += dp[d[C[i]]]
      dp[i] %= mod
    d[C[i]] = i
  return dp[-1]
print(solve())