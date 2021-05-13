h,w=map(int,input().split())
l=[list(input()) for i in range(h)]
connection=[[] for i in range(h*w)]
start=[]

for i in range(h):
  for j in range(w):
    if i!=0:
      connection[i*w+j].append((i-1)*w+j)
    if i!=h-1:
      connection[i*w+j].append((i+1)*w+j)
    if j!=0:
      connection[i*w+j].append(i*w+j-1)
    if j!=w-1:
      connection[i*w+j].append(i*w+j+1)
    if l[i][j]=='#':
      start.append(i*w+j)
n=h*w

def bfs(l):
  distance=[-1]*n
  next=set()
  next2=set()
  visited=[-1]*n
  visitct=0
  for i in range(len(l)):
    distance[l[i]]=0
    for j in range(len(connection[l[i]])):
      next.add(connection[l[i]][j])
    visited[l[i]]=1
    visitct=+1
  next=list(next)
  ct=0
  while len(next)!=0 and visitct!=n:
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

print(max(bfs(start)))