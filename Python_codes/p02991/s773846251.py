from collections import deque
n, m = map(int, input().split())

g = [[] for i in range(n)]

for i in range(m):
  u, v = map(int, input().split())
  u, v = u-1, v-1
  g[u].append(v)
# print(g)

s, t = map(int, input().split())
s, t = s-1, t-1

visited = [[-1]*3 for j in range(n)]

l = 0
queue = deque([[s, l]])
visited[s][l] = 0
while queue:
  x, l = queue.popleft()
  if [x, l] == [t, 0]:
    print(visited[x][l]//3)
    exit()
  for x_ in g[x]:
    new_x, new_l = x_, (l+1)%3
    if visited[new_x][new_l] == -1:
      visited[new_x][new_l] = visited[x][l]+1
      queue.append([new_x, new_l])
    
print(visited[t][0])