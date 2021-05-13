MOD = 1000000007
h,w=map(int,input().split())
graph=[]
for i in range(h):
  graph.append(list(input()))
#print(graph)
dp=[[0]*(w) for _ in range(h)]
dp[0][0]=1
for i in range(1,w):
  if graph[0][i]=='#':
    break
  dp[0][i]=1
for i in range(1,h):
  if graph[i][0]=='#':
    break
  dp[i][0]=1
for i in range(1,h):
  for j in range(1,w):
    #print(i-1,j-1)
    if(graph[i][j]=='#'):
      dp[i][j]=0
    else:
      dp[i][j]=(dp[i-1][j]+dp[i][j-1])%MOD

print(dp[-1][-1])