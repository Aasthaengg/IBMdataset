def solve():
  N, K = map(int, input().split())
  H = list(map(int, input().split()))
  dp = [float('inf')]*N
  dp[0]=0
  for i in range(N):
    for k in range(1,K+1):
      if i+k<N:
        dp[i+k] = min(dp[i+k],dp[i]+abs(H[i+k]-H[i]))
  ans = dp[N-1]
  return ans
print(solve())