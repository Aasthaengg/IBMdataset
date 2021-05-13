from collections import deque

N, M = map(int, input().split())
routes = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  routes[a].append(b)
  routes[b].append(a)
checked = [0 for _ in range(N+1)]
route = deque(routes[1])
for r in routes[1]:
  checked[r] = 1
while(len(route) > 0):
  r = route.popleft()
  for rr in routes[r]:
    if checked[rr] == 0:
      checked[rr] = r
      route.append(rr)
for i in range(2, N+1):
  if checked[i] == 0:
    print('No')
    exit()
print('Yes')
for j in range(2, N+1):
  print(checked[j])
