import sys
sys.setrecursionlimit(100001)

def dfs(node,w):
  weight = w
  for l in tree[node]:
    if color[l[0]] > -1:
      continue
    if l[1]%2 == 0:
      color[l[0]] = color[node]
    else:
      color[l[0]] = int(not color[node])
    dfs(l[0],l[1])
    


N = int(input())
tree = {}
color = [-1]*(N+1)

for i in range(1,N+1):
  tree[i] = []
for i in range(N-1):
  u,v,w = map(int,input().split())
  tree[u].append([v,w])
  tree[v].append([u,w])
  
color[1] = 0
dfs(1,0)
color = [c  if c>-1 else 0 for c in color]
print('\n'.join(map(str,color[1:])))