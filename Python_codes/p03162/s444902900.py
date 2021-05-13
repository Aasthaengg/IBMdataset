INF = 10**9
N = int(input())
happiness = [[0, 0, 0]]
for _ in range(N):
  happiness.append(list(map(int, input().split())))
dp = [[-INF] * 3 for _ in range(N+1)]
dp[0] = [0, 0, 0]

for i in range(1, N+1):
  dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + happiness[i][0]
  dp[i][1] = max(dp[i-1][2], dp[i-1][0]) + happiness[i][1]
  dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + happiness[i][2]
print(max(dp[N]))