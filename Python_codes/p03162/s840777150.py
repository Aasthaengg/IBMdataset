n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
dp=[[a[0][0],a[0][1],a[0][2]]]+[[0]*3 for i in range(n-1)]
for i in range(1,n):
  for j in range(3):
    if j==0:
      dp[i][j]=max(dp[i-1][1],dp[i-1][2])+a[i][0]
    elif j==1:
      dp[i][j]=max(dp[i-1][0],dp[i-1][2])+a[i][1]
    else:
      dp[i][j]=max(dp[i-1][1],dp[i-1][0])+a[i][2]
print(max(dp[n-1]))