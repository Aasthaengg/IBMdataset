def solve():
  N = int(input())
  H = list(map(int, input().split()))
  dp = [float('inf')]*N
  dp[0]=0
  for i in range(N):
    if i+1<N:
      dp[i+1] = min(dp[i+1],dp[i]+abs(H[i+1]-H[i]))
    if i+2<N:
      dp[i+2] = min(dp[i+2],dp[i]+abs(H[i+2]-H[i]))
  ans = dp[N-1]
  return ans
print(solve())