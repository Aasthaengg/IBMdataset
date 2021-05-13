from collections import deque

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
routings = [[] for _ in range(N+1)]
for a, b in edges:
  routings[a].append(b)
  routings[b].append(a)

answer = 0
for a, b in edges:
  route = deque([])
  cnt = 0
  checked = [False for i in range(N+1)]
  for r in routings[1]:
    if a == 1 and b == r:
      continue
    else:
      route.append(r)
      cnt += 1
      checked[r] = True
  while len(route) > 0:
    current = route.popleft()
    for next in routings[current]:
      if not checked[next] and (min(current, next) != a or max(current, next) != b):
        route.append(next)
        cnt += 1
        checked[next] = True
  if cnt < N:
    answer += 1
print(answer)
