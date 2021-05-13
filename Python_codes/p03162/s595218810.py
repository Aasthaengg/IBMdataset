n=int(input())
a,b,c=map(int,input().split())
dp=[[0]*3 for i in range(n)]
dp[0][0],dp[0][1],dp[0][2]=a,b,c

for i in range(1,n):
  a,b,c=map(int,input().split())
  for j in range(3):
    if j==0:
      dp[i][j]=max(dp[i-1][1],dp[i-1][2])+a
    elif j==1:
      dp[i][j]=max(dp[i-1][0],dp[i-1][2])+b
    else:
      dp[i][j]=max(dp[i-1][0],dp[i-1][1])+c
      
print(max(dp[-1]))