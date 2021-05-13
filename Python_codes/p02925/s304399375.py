N=int(input())

a=[[0 for j in range(N-1)] for i in range(N)]
for i in range(N):
  line=list(map(int,input().split()))
  for j in range(N-1):
    a[i][j]=line[j]-1

id=[[0 for j in range(N)] for i in range(N)]
v=0
for i in range(N-1):
  for j in range(i+1,N):
    id[i][j]=v
    v+=1

def toId(i,j):
  if i>j:
    i,j=j,i
  return id[i][j]

to=[[] for i in range(v)]
inner=[0 for i in range(v)]
for i in range(N):
  for j in range(N-1):
    a[i][j]=toId(i,a[i][j])
  for j in range(N-2):
    to[a[i][j]].append(a[i][j+1])
    inner[a[i][j+1]]+=1

stack=[]
isstarted=[False for i in range(v)]
dist=[0 for i in range(v)]
for i in range(v):
  if inner[i]==0:
    stack.append([i,1])

while stack:
  node=stack.pop()
  e=node[0]
  d=node[1]
  if d>dist[e]:
    dist[e]=d
  inner[e]-=1
  if inner[e]<=0 and not isstarted[e]:
    isstarted[e]=True
    children=to[e]
    for child in children:
      stack.append([child,dist[e]+1])
for i in range(len(isstarted)):
  if not isstarted[i]:
    print(-1)
    break
else:
  ans=0
  for i in range(len(dist)):
    if dist[i]>ans:
      ans=dist[i]
  print(ans)