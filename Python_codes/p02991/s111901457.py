n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]
s,t=map(int,input().split())

connection=[[] for i in range(3*n)]
for i in range(m):
  connection[l[i][0]-1].append(l[i][1]-1+n)
  connection[l[i][0]-1+n].append(l[i][1]-1+2*n)
  connection[l[i][0]-1+2*n].append(l[i][1]-1)

def bfs(v):
  distance=[-1]*(3*n)
  distance[v]=0
  next=connection[v]
  next2=set()
  visited=[-1]*(3*n)
  visited[v]=1
  visitct=1
  ct=0
  while len(next)!=0 and visitct!=3*n:
    ct+=1
    for i in range(len(next)):
      if visited[next[i]]==-1:
        distance[next[i]]=ct
        visited[next[i]]=1
        visitct+=1
        for j in range(len(connection[next[i]])):
          if visited[connection[next[i]][j]]==-1:
            next2.add(connection[next[i]][j])
    next=list(next2)
    next2=set()
  return distance

if bfs(s-1)[t-1]==-1 or bfs(s-1)[t-1]%3!=0:
  print(-1)
else:
  print(bfs(s-1)[t-1]//3)