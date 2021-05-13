import sys
readline = sys.stdin.readline

N = int(readline())
P = list(map(float,readline().split()))

# dp[i][j] = i枚投げて、表がj枚出ている確率
dp = [[0] * (N + 1) for i in range(N + 1)]
dp[0][0] = 1
for i in range(N):
  for j in range(N):
    dp[i + 1][j] += dp[i][j] * (1 - P[i])
    dp[i + 1][j + 1] += dp[i][j] * P[i]
    
ans = 0
for i in range(N + 1):
  if i > N // 2:
    ans += dp[-1][i]

print(ans)