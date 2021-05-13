n=int(input())
dp=[[0,0,0] for _ in range(n)]
for i in range(n):
  if i==0:
    dp[i]=list(map(int,input().split()))
  else:
    abc=list(map(int,input().split()))
    dp[i][0]=max(dp[i-1][1],dp[i-1][2])+abc[0]
    dp[i][1]=max(dp[i-1][0],dp[i-1][2])+abc[1]
    dp[i][2]=max(dp[i-1][1],dp[i-1][0])+abc[2]
answer=0
for j in range(3):
  answer=max(answer,dp[-1][j])
print(answer)