def solve():
  R, C, K = map(int, input().split())
  item = [[0]*C for _ in range(R)]
  for i in range(K):
    r,c,v = map(int, input().split())
    item[r-1][c-1] = v
  dp = [[[0]*(C+1) for _ in range(R+1)] for _ in range(4)]
  for i in range(1,R+1):
    for j in range(1,C+1):
      for k in range(4): #横から取らない
        dp[k][i][j] = dp[k][i][j-1]
      #上から取らない
      dp[0][i][j] = max(dp[0][i][j],dp[-1][i-1][j])
      if item[i-1][j-1]>0:
        #上からとる
        dp[1][i][j] = max(dp[1][i][j],dp[-1][i-1][j]+item[i-1][j-1])
        for k in range(1,4): #横から取る
          dp[k][i][j] = max(dp[k][i][j],dp[k-1][i][j-1]+item[i-1][j-1])
      for k in range(1,4):
        dp[k][i][j] = max(dp[k-1][i][j],dp[k][i][j])
  ans = 0
  for k in range(4):
    ans = max(ans,dp[k][-1][-1])
  return ans
print(solve())