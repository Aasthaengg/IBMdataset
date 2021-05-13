N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

#i回目、jの手を出した時の点数の最大値
dp = [[0]*3 for _ in range(N)]

for i in range(N):
  if i>=1:
    dp[i][0] += max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
    dp[i][1] += max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
    dp[i][2] += max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
    
  if T[i] == "s":
    dp[i][0] += R
  if T[i] == "p":
    dp[i][1] += S
  if T[i] == "r":
    dp[i][2] += P
    
  if i-K >= 0:
    dp[i][0] += max(dp[i-K][1],dp[i-K][2]) - max(dp[i-K][0],dp[i-K][1],dp[i-K][2])
    dp[i][1] += max(dp[i-K][2],dp[i-K][0]) - max(dp[i-K][0],dp[i-K][1],dp[i-K][2])
    dp[i][2] += max(dp[i-K][0],dp[i-K][1]) - max(dp[i-K][0],dp[i-K][1],dp[i-K][2])
  
print(max(dp[-1][0],dp[-1][1],dp[-1][2]))