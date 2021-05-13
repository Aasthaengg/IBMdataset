N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0 for i in range(N)]
for i in range(1, N):
  buf = dp[i-1] + abs(A[i]-A[i-1])
  for k in range(2,K+1):
    if i-k < 0:
      break
    buf = min(buf, dp[i-k] + abs(A[i]-A[i-k]))
  dp[i] = buf
print(dp[N-1])