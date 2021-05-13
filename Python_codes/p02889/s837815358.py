import sys
input=sys.stdin.readline
n,m,l=map(int,input().split())
INF=10**10
graph=[[INF for i in range(n)] for j in range(n)]
fuel=[[INF for i in range(n)] for j in range(n)]
#for i in range(n):
#    graph[i][i]=0
for i in range(m):
    a,b,c=map(int,input().split())
    a-=1;b-=1
    if c>l:continue
    graph[a][b],graph[b][a]=c,c
for i in range(n):
  for j in range(n):
    for k in range(n):
      graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])
for i in range(n):
    for j in range(n):
        if graph[i][j]<=l:
            fuel[i][j]=1
for i in range(n):
  for j in range(n):
    for k in range(n):
      fuel[j][k]=min(fuel[j][k],fuel[j][i]+fuel[i][k])
q=int(input())
for i in range(q):
    s,t=map(int,input().split())
    s-=1;t-=1
    if fuel[s][t]==INF:print(-1)
    else:print(fuel[s][t]-1)