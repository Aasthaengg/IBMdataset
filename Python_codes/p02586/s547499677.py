import sys
input=lambda:sys.stdin.readline().rstrip()
r,c,k=map(int,input().split())
dp=[[(c+1)*[0]for _ in range(r+1)]for _ in range(4)]
p=[c*[0]for _ in range(r)]
for _ in range(k):
  rr,cc,u=map(int,input().split())
  rr-=1
  cc-=1
  p[rr][cc]=u
ans=0
for j in range(1,r+1):
  for k in range(1,c+1):
    dp[0][j][k]=max(dp[0][j-1][k],dp[0][j][k-1])
    t=max(dp[0][j-1][k],dp[1][j-1][k],dp[2][j-1][k],dp[3][j-1][k])
    for i in range(1,4):
      dp[i][j][k]=max(dp[i][j][k],t,dp[i][j][k-1])
      if p[j-1][k-1]:
        dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k-1]+p[j-1][k-1],t+p[j-1][k-1])
      ans=max(ans,dp[i][j][k])
print(ans)
