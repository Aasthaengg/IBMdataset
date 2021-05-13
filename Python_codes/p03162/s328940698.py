N=int(input())
abc=[tuple(map(int,input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

for i in range(N):
  for j in range(3):
    if i == 0:
      dp[i][j] = abc[i][j]
      continue
    op1, op2 = [(1,2),(0,2),(0,1)][j]
    dp[i][j] = max(dp[i-1][op1], dp[i-1][op2])+abc[i][j]
    
print(max(dp[-1]))