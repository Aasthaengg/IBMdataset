from collections import deque

N, M = map(int, input().split())

graph = [[] for i in range(N)]
for i in range(M):
  u, v = map(int, input().split())
  graph[u-1].append(v-1)

s, t = map(int, input().split())
s -= 1
t -= 1


is_visited = [[False]*N for i in range(3)]
is_visited[0][s] = True

d = deque([s])
ans = 0
while d:
  ans += 1
  for step in [1, 2, 0]:
    diff = 0
    if d:
      len_d = len(d)
      for i in range(len_d):
        node = d.popleft()
        children = graph[node]
        for child in children:
          if step == 0:
            if child == t:
              d = []
              diff = 1
              break
          
          if not is_visited[step][child]:
            is_visited[step][child] = True
            diff += 1
            d.append(child)
          
        else:
          continue
        break
    
    else:
      ans = -1
      break
  
  if not diff:
    ans = -1
    break

print(ans)