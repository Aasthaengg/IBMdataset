def dfs(node):
  visited[node]=True
  stack=[node]
  while stack:
    node=stack.pop()
    for child in g[node]:
      if visited[child]==False:
        visited[child]=True
        stack.append(child)
n,m=map(int,input().split())
g={i:[] for i in range(1,n+1)}
for i in range(m):
  u,v=map(int,input().split())
  g[u].append(v)
  g[v].append(u)
visited=[False for i in range(n+1)]
c=0
for i in range(1,n+1):
  if visited[i]==False:
    c=c+1
    dfs(i)
print(c-1)