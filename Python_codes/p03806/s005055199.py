n,ma,mb=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
suma=0;sumb=0
for i in range(n):
  suma+=l[i][0]
  sumb+=l[i][1]
dp=[[[float('inf') for i in range(sumb+1)] for i in range(suma+1)] for i in range(n+1)]
dp[0][0][0]=0
for i in range(n):
  for j in range(suma):
    for k in range(sumb):
      dp[i+1][j][k]=min(dp[i+1][j][k],dp[i][j][k])
      if j+l[i][0]<=suma and k+l[i][1]<=sumb:
        dp[i+1][j+l[i][0]][k+l[i][1]]=min(dp[i+1][j+l[i][0]][k+l[i][1]],dp[i][j][k]+l[i][2])
ans=[]
for j in range(suma+1):
  for k in range(sumb+1):
    if j*mb==k*ma and j*j!=0:
      ans.append(dp[n][j][k])
if min(ans)==float('inf'):
  print(-1)
else:
  print(min(ans))