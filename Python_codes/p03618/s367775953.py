from collections import defaultdict

A = input()
N = len(A)
dp = [0] * N
dp[0] = 1
d = defaultdict(int)
d[A[0]] = 1

for i in range(1, N):
  a = A[i]
  dp[i] = dp[i-1]
  dp[i] += i - d[a]
  d[a] += 1

print(dp[-1])