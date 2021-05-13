def solve():
  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  dp = ['Second']*(K*2)
  for i in range(K):
    if dp[i]!='Second':
      continue
    for j in range(N):
      dp[i+A[j]]='First'
  ans = dp[K]
  return ans
print(solve())