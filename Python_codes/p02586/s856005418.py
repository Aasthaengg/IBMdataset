R, C, K=map(int, input().split())
math=[[0]*C for _ in range(R)]
for _ in range(K):
  r, c, v=map(int, input().split())
  math[r-1][c-1]=v
  
dp=[[[0]*C for __ in range(R)] for _ in range(4)]
if math[0][0]>0:
  dp[1][0][0]=math[0][0]+0
  
for j in range(1, C):
  dp[0][0][j]=dp[0][0][j-1]+0
  dp[1][0][j]=max(dp[1][0][j-1], dp[0][0][j-1]+math[0][j])
  dp[2][0][j]=max(dp[2][0][j-1], dp[1][0][j-1]+math[0][j])
  dp[3][0][j]=max(dp[3][0][j-1], dp[2][0][j-1]+math[0][j])
    
for i in range(1, R):
  dp[0][i][0]=max(dp[0][i-1][0], dp[1][i-1][0], dp[2][i-1][0], dp[3][i-1][0])
  dp[1][i][0]=dp[0][i][0]+math[i][0]
  for j in range(1, C):
    dp[0][i][j]=max(dp[0][i][j-1], max(dp[0][i-1][j], dp[1][i-1][j], dp[2][i-1][j], dp[3][i-1][j]))
    dp[1][i][j]=max(dp[1][i][j-1], dp[0][i][j-1]+math[i][j], max(dp[0][i-1][j], dp[1][i-1][j], dp[2][i-1][j], dp[3][i-1][j])+math[i][j])
    dp[2][i][j]=max(dp[2][i][j-1], dp[1][i][j-1]+math[i][j])
    dp[3][i][j]=max(dp[3][i][j-1], dp[2][i][j-1]+math[i][j])
    
print(max(dp[0][-1][-1], dp[1][-1][-1], dp[2][-1][-1], dp[3][-1][-1]))