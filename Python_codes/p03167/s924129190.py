H,W = map(int,input().split())
field = ["#"*(W+2)]
field += ["#"+input()+"#" for _ in range(H)]
field += ["#"*(W+2)]
dp = [[0]*(W+2) for _ in range(H+2)]
dp[1][1] = 1

#i,jへの最短経路の個数
for i in range(H+2):
  for j in range(W+2):
    if field[i][j] == ".":
      dp[i][j] = max(dp[i-1][j] + dp[i][j-1],dp[i][j])
    
print(dp[H][W]%1000000007)