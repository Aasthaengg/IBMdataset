import sys
sys.setrecursionlimit(4000)

def dfs(now):
  v[now]=0
  for i in edge[now]:
    if v[i]:
      point[i]+=point[now]
      dfs(i)

n,q=map(int,input().split())
edge=[[] for _ in range(n)]
point=[0]*n
for i in range(n-1):
  a,b=map(int,input().split())
  edge[a-1].append(b-1)
  edge[b-1].append(a-1)
for i in range(q):
  p,x=map(int,input().split())
  point[p-1]+=x
v=[1]*n
queue=[0]
v[0]=0
while queue:
  now=queue.pop()
  for i in edge[now]:
    if v[i]:
      v[i]=0
      queue.append(i)
      point[i]+=point[now]
print(*point)