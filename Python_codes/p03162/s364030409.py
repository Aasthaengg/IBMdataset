N=int(input())
happy=[]
dp=[[0,0,0] for r in range(N)]
for i in range(N):
  happy.append(list(map(int,input().split())))
dp[0]=happy[0].copy()
for i in range(1,N):
  for j in range(3):
    for k in range(3):
      if j != k :
        dp[i][j]=max(dp[i-1][k]+happy[i][j],dp[i][j])
        

  
print(max(dp[N-1]))