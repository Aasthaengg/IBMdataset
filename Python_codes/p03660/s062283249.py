import collections
n=int(input())
graph=[]
for i in range(n+1):
  graph.append([])
for i in range(n-1):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
dist1=[0]*(n+1)
distn=[0]*(n+1)
bfs=collections.deque([[1,0]])
visited=set()
while bfs:
  s=bfs.popleft()
  visited.add(s[0])
  dist1[s[0]]=s[1]
  for i in graph[s[0]]:
    if i in visited:
      continue
    bfs.append([i,s[1]+1])
bfs=collections.deque([[n,0]])
visited=set()
while bfs:
  s=bfs.popleft()
  visited.add(s[0])
  distn[s[0]]=s[1]
  for i in graph[s[0]]:
    if i in visited:
      continue
    bfs.append([i,s[1]+1])
score1=0
scoren=0
for i in range(1,n+1):
  if dist1[i]>distn[i]:
    scoren+=1
  else:
    score1+=1
if scoren>=score1:
  print('Snuke')
else:
  print('Fennec')