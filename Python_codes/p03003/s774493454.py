N, M = map(int, input().split())
s = [int(c) for c in input().split()]
t = [int(c) for c in input().split()]
MOD = 10**9+7

dp = [[0]*(M+1) for i in range(N+1)]
dp_cum = [[0]*(M+1) for i in range(N+1)]

dp[0][0] = 1
for i in range(N+1):
  dp_cum[i][0] = 1
for j in range(M+1):
  dp_cum[0][j] = 1
  
for i in range(N):
  for j in range(M):
    if s[i]!=t[j]:
      dp[i+1][j+1] = 0
    else:
      dp[i+1][j+1] = dp_cum[i][j]
    dp_cum[i+1][j+1] = dp_cum[i][j+1] + dp_cum[i+1][j] - dp_cum[i][j] + dp[i+1][j+1]
    dp_cum[i+1][j+1] %= MOD

print(dp_cum[-1][-1])