from collections import deque
H,W = map(int,input().split()); INF = float("inf")
G = []
for i in range(H):
  temp = str(input()); temp = list(temp)
  G.append(temp)

dp = [[INF]*W for _ in range(H)]
dp[0][0] = 0
if G[0][0] == "#":
  dp[0][0] += 1
for i in range(H):
  for j in range(W):
    #横への遷移
    if j+1 <= W-1: #一番右以外
      if G[i][j] == "." and G[i][j+1] == "#":
        dp[i][j+1] = min(dp[i][j+1],dp[i][j] + 1)
      else:
        dp[i][j+1] = min(dp[i][j+1],dp[i][j])
    #下への遷移
    if i+1 <= H-1: #一番右以外
      if G[i][j] == "." and G[i+1][j] == "#":
        dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
      else:
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
#print(dp)
ans = dp[-1][-1]
print(ans)