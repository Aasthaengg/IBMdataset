N,M = map(int, input().split())
ng = set()
for i in range(M):
  ng.add(int(input()))
  
dp = [0] * (N + 5)
dp[0] = 1

for i in range(N):
  for j in range(1, 3):
    if (i + j) not in ng:
      dp[i + j] += dp[i]
      dp[i + j] %= 1000000007

print(dp[N])