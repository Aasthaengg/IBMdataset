n,p = map(int,input().split())
a_list = list(map(int,input().split()))
dp = [[0,0] for i in range(n+1)]
dp[0][0] = 1
dp[0][1] = 0
for i in range(n):
  if a_list[i] % 2 == 0:
    dp[i+1][0] = dp[i][0] + dp[i][0] 
    dp[i+1][1] = dp[i][1] + dp[i][1]
  if a_list[i] % 2 == 1:
    dp[i+1][0] = dp[i][0] + dp[i][1] 
    dp[i+1][1] = dp[i][1] +dp[i][0] 
    
print(dp[-1][p])