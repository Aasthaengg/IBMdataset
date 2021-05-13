n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
   a, b = map(int, input().split())
   edges[a-1].append(b-1)
   edges[b-1].append(a-1)

# bfs
def bfs(v):
   dist = [-1] * n
   dist[v] = 0
   visit = [v]
   c = 1
   while visit:
      next = []
      for i in visit:
         for j in edges[i]:
            if dist[j] == -1:
               dist[j] = c
               next.append(j)
      visit = next
      c += 1
      if c > 2:
         break

   return dist

dist = bfs(0)
if dist[-1] == -1:
   print('IMPOSSIBLE')
else:
   print('POSSIBLE')
