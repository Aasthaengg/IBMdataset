from collections import deque
n=int(input())
edge=[]
graph=[[] for i in range(n)]
point=[-1]*n
for i in range(n-1):
  a,b=map(int,input().split())
  a-=1;b-=1
  edge.append([a,b])
  graph[a].append(b)
  graph[b].append(a)
num=list(map(int,input().split()));num.sort()
start=0
for i in range(n):
  if len(graph[i])==1:
    start=i
    break
dfs=deque([start])
while dfs:
  v=dfs.popleft()
  point[v]=num.pop()
  for i in graph[v]:
    if point[i]!=-1:continue
    dfs.appendleft(i)
ans=0
for i in edge:
  ans+=min(point[i[0]],point[i[1]])
print(ans)
print(*point)