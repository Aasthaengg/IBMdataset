def solve():
  N = int(input())
  dp = [[float('inf')]*3 for _ in range(N)]
  dp[0] = list(map(int, input().split()))
  for i in range(1,N):
    a, b, c = map(int, input().split())
    dp[i][0] = max(dp[i-1][1],dp[i-1][2])+a
    dp[i][1] = max(dp[i-1][0],dp[i-1][2])+b
    dp[i][2] = max(dp[i-1][0],dp[i-1][1])+c
  ans = max(dp[-1])
  return ans
print(solve())