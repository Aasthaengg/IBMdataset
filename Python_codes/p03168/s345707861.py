# dp[i][j]：i枚で表がj枚になる確率
# 1 - sum(:dp[N][(N+1)//2])を求めればいいため，dp[N][(N+1)//2:]は求める必要が無い
# jが大きい順に更新すればdp[i][j]のjを保持する必要はない

N = int(input())
P = list(map(float, input().split()))
overhalf_N = (N+1)//2
underhalf_N = overhalf_N - 1

dp = [0]*(N+1) # dp[N][j]：N枚で表がj枚になる確率

dp[0] = 1
for i in range(overhalf_N):
  pc = 1 - P[i]
  for j in range(i+1, 0, -1):
    dp[j] = dp[j-1] * P[i] + dp[j] * pc
  dp[0] = dp[0] * pc

for i in range(overhalf_N,N):
  pc = 1 - P[i]
  for j in range(underhalf_N, 0, -1):
    dp[j] = dp[j-1] * P[i] + dp[j] * pc
  dp[0] = dp[0] * pc

print(1-sum(dp[:overhalf_N]))
