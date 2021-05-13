n = int(input())
abc = [list(map(int, input().split())) for i in range(n-1)]
q,k = map(int, input().split())
tree = [list() for i in range(n+1)]
visited = [0] * (n+1)
dist = [0] * (n+1)
for a,b,c in abc:
  tree[a].append((b,c))
  tree[b].append((a,c))
stack = [k]
visited[k] = 1
while stack:
  now = stack.pop()
  for NEXT,d in tree[now]:
    if not visited[NEXT]:
      visited[NEXT] = 1
      dist[NEXT] = dist[now] + d
      stack.append(NEXT)
for i in range(q):
  x,y = map(int, input().split())
  print(dist[x]+dist[y])
