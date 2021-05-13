H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]
INF=10001
dp = [[INF]*W for _ in range(H)]
dp[0][0] = 0 if S[0][0] == "." else 1
 
for i in range(H):
  for j in range(W):
    m,n=INF,INF
    if i != 0:
      m = dp[i-1][j] + (S[i-1][j] == "." and S[i][j] == "#")
    if j != 0:
      n = dp[i][j-1] + (S[i][j-1] == "." and S[i][j] == "#")
 
    dp[i][j] = min(m, n, dp[i][j])
  
print(dp[H-1][W-1])