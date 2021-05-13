N = int(input())
dp = [[[[0 for a in range(4)] for b in range(4)] for c in range(4)] for i in range(100+1)]
#A,G,C,T: 0,1,2,3

mod = 10**9 + 7

for a in range(4):
  for b in range(4):
    for c in range(4):
      dp[3][a][b][c] = 1
dp[3][0][1][2] = 0
dp[3][0][2][1] = 0
dp[3][1][0][2] = 0
#print(dp[3])

for i in range(4,100+1):
  for a in range(4):
    for b in range(4):
      for c in range(4):
        for j in range(4):
          dp[i][a][b][c] += dp[i-1][j][a][b]
          if b == 1 and c == 2 and j == 0:
            dp[i][a][b][c] -= dp[i-1][j][a][b]
          if a == 1 and c == 2 and j == 0:
            dp[i][a][b][c] -= dp[i-1][j][a][b]
          if a == 1 and b == 1 and c == 2 and j == 0:
            dp[i][a][b][c] += dp[i-1][j][a][b]
          dp[i][a][b][c] %= mod
  dp[i][0][1][2] = 0
  dp[i][1][0][2] = 0
  dp[i][0][2][1] = 0

answer = 0
for a in range(4):
  for b in range(4):
    for c in range(4):
      answer += dp[N][a][b][c]
answer %= mod
print(answer)