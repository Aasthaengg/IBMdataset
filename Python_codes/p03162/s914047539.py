n = int(input())
act = []
dp = [[0]*3 for i in range(n)]
for _ in range(n):
  a,b,c = map(int,input().split())
  act.append([a,b,c])
a,b,c = act[0]
dp[0][0],dp[0][1],dp[0][2] = a,b,c
for i in range(1,n):
  dp[i][0] = max(dp[i-1][1]+act[i][0], dp[i-1][2]+act[i][0])
  dp[i][1] = max(dp[i-1][0]+act[i][1], dp[i-1][2]+act[i][1])
  dp[i][2] = max(dp[i-1][0]+act[i][2], dp[i-1][1]+act[i][2])
print(max(dp[-1][0], dp[-1][1], dp[-1][2]))