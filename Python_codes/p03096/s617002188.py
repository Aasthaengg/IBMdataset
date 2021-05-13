from itertools import groupby

n = int(input())
C = [key for key, _ in groupby([int(input()) for _ in range(n)])]

N = len(C)

MOD = 10 ** 9 + 7

dp = [0 for _ in range(N)]
dp[0] = 1

T = {}
T[C[0]] = 0

for i in range(1, N):
  if i == 0 or C[i - 1] == C[i] or C[i] not in T:
    dp[i] = dp[i - 1]
  else:
    j = T[C[i]]
    dp[i] = dp[i - 1] + dp[j]
  dp[i] %= MOD
  T[C[i]] = i

print(dp[N - 1])