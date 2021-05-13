N = int(input())
A = [int(input()) for _ in range(N)]

MOD = 10**9 + 7

dp = [0] * N
prev_i = [-1] * (2 * 10**5 + 1)

dp[0] = 1
prev_i[A[0]] = 0

for i in range(1, N):
  a = A[i]
  if prev_i[a] >= 0:
    if prev_i[a] == i - 1:
      dp[i] = dp[i - 1]
    else:
      dp[i] = dp[i - 1] + dp[prev_i[a]]
  else:
    dp[i] = dp[i - 1]
  prev_i[a] = i
  #print(i, dp, prev_i)

print(dp[-1] % MOD)