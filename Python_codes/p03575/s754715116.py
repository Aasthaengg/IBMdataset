N,M = map(int,input().split())

road = [[] for _ in range(N)]

for _ in range(M):
  a,b = map(int,input().split())
  road[a-1].append(b-1)
  road[b-1].append(a-1)

def dfs(v,w):
  l = [0 for _ in range(N)]
  l[v] = 1
  stack = [v]
  while stack:
    vv = stack.pop()
    for i in road[vv]:
      if i == w and v == vv or i == vv and v == w:
        continue
      else:
        if l[i] == 0:
          l[i] = 1
          stack.append(i)
  return sum(l)

ans = 0
check = [[0 for _ in range(N)] for _ in range(N)]

for n in range(N):
  for m in range(len(road[n])):
    if check[n][road[n][m]] == 0 or check[road[n][m]][n] == 0:
      check[n][road[n][m]] = 1
      check[road[n][m]][n] = 1
      d = dfs(n,road[n][m])
      if d != N:
        ans += 1

print(ans)