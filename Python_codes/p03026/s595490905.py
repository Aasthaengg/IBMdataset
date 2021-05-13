from collections import deque
n = int(input())
ab = [list(map(int,input().split())) for i in range(n-1)]
c = list(map(int,input().split()))
c.sort(reverse=True)
graph = [[] for i in range(n+1)]
parent = [0 for i in range(n+1)]
root = 1
order = []
que = deque([root])
for a,b in ab:
  graph[a].append(b)
  graph[b].append(a)
while que:
  x = que.popleft()
  order.append(x)
  for y in graph[x]:
    if parent[x] == y:
      continue
    parent[y] = x
    que.append(y)
ans = []
for i in range(n):
  ans.append((order[i],c[i]))
ans.sort()
print(sum(c[1:]))
for i in ans:
  print(i[1],end=" ")