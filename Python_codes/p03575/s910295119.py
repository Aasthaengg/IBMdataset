n,m = map(int,input().split())
g = [[] for i in range(n)]
ab = []
for k in range(m):
  i,j = map(int,input().split())
  i,j = i-1,j-1
  g[i].append(j)
  g[j].append(i)
  ab.append((i,j))
c = 0
for i in range(m):
  visited = [1]+[0]*(n-1)
  stack = [0]
  while stack:
    cur = stack.pop()
    for j in g[cur]:
      if ab[i] in [(cur,j),(j,cur)]:
        continue
      if visited[j] == 0:
        visited[j] = 1
        stack.append(j)
  if 0 in visited:
    c += 1
print(c)