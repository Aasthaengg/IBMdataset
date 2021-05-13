n =int(input())
l = [list(map(int,input().split())) for i in range(n)]

dp = [[0 for i in range(3)] for j in range(n)]

for i in range(n):
  if i==0:
    dp[0]=l[0]
  else:
    dp[i][0]=max(dp[i][0],dp[i-1][1]+l[i][0],dp[i-1][2]+l[i][0])
    dp[i][1]=max(dp[i][1],dp[i-1][0]+l[i][1],dp[i-1][2]+l[i][1])
    dp[i][2]=max(dp[i][2],dp[i-1][0]+l[i][2],dp[i-1][1]+l[i][2])
print(max(dp[n-1]))