N,M,L=map(int,input().split())
X=[list(map(int,input().split())) for i in range(N)]
INF=10**9
DP=[[INF]*411 for i in range(411)]
DP[0][0]=0
for i in range(N):
  for j in range(400,-1,-1):
    for k in range(401):
      DP[j+X[i][0]][k+X[i][1]]=min(DP[j+X[i][0]][k+X[i][1]],DP[j][k]+X[i][2])
P=INF
for i in range(1,401):
  if i*max(M,L)>400:
    break
  P=min(P,DP[i*M][i*L])
if P==INF:
  print(-1)
else:
  print(P)