N = int(input())
AB = [list(map(int, input().split())) for _ in range(N -1)]

graph = [[] for _ in range(N + 1)]
for a, b in AB:
  graph[a].append(b)
  graph[b].append(a)

def dfs(n):
  INF = 10 ** 10
  dist = [INF] * (N + 1)

  stack = [n]
  dist[n] = 0
  while stack:
    s = stack.pop()
    for g in graph[s]:
      if dist[s] + 1 < dist[g]:
        stack.append(g)
        dist[g] = dist[s] + 1
  return dist

dist_f = dfs(1)
dist_a = dfs(N)
D = dist_f[N]
#print("dist_f:", dist_f)
#print("dist_a:", dist_a)

f_cnt = 0
a_cnt = 0

color = [0] * (N + 1)
color[1] = 1
color[N] = -1

for i in range(1, N + 1):
  if dist_f[i] <= D // 2:
    if color[i] == 0:
      f_cnt += 1
      color[i] = 1
  if dist_a [i] <= (D - 1) // 2:
    if color[i] == 0:
      a_cnt += 1
      color[i] = -1
#print("color:", color)
#print("f_cnt, a_cnt:", f_cnt, a_cnt)

def paint(n):
  cnt = 0
  for i in range(1, N + 1):
    if color[i] == n:
      stack = [i]
      while stack:
        s = stack.pop()
        for g in graph[s]:
          if color[g] == 0:
            stack.append(g)
            color[g] = n
            cnt += 1
  return cnt

f_cnt += paint(1)
a_cnt += paint(-1)

if f_cnt >= a_cnt + 1:
  print("Fennec")
else:
  print("Snuke")