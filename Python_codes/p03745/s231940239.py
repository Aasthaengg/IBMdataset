N = int(input())
A = list(map(int, input().split()))

dp = [[N, N] for i in range(N)]
dp[0] = [1, 1]
for i, a in enumerate(A[1:], 1):
  pre_a = A[i-1]
  if pre_a < a:
    dp[i][0] = min(dp[i-1][0], dp[i-1][1]+1)
    dp[i][1] = min(dp[i-1][0]+1, dp[i-1][1]+1)
  elif pre_a == a:
    dp[i][0] = min(dp[i-1][0], dp[i-1][1]+1)
    dp[i][1] = min(dp[i-1][0]+1, dp[i-1][1])
  else:
    dp[i][0] = min(dp[i-1][0]+1, dp[i-1][1]+1)
    dp[i][1] = min(dp[i-1][0]+1, dp[i-1][1])

print(min(dp[-1]))