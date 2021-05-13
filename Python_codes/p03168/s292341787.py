N = int(input())
p = list(map(float, input().split()))

dp = [[0 for i in range(N+1)] for j in range(N+1)]
dp[0][0] = 1

for i in range(1,N+1):
  for j in range(i+1):
    if j == 0:
      dp[j][i] = (1-p[i-1])*dp[j][i-1]
    else:
      dp[j][i] = (1-p[i-1])*dp[j][i-1] + p[i-1]*dp[j-1][i-1]

sum_ = 0
for i in range(N//2+1, N+1):
  sum_ += dp[i][-1]

print(sum_)