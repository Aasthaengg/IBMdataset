from collections import defaultdict as dd
N, M = map(int, input().split())
e = dd(list)
inf = 10 ** 9
pos = [inf] * (N + 1)
for i in range(M):
  a, b, d = map(int, input().split())
  e[a].append((b, d))
  e[b].append((a, -d))
visited = [0] * (N + 1)
s = []
for i in range(1, N + 1):
  if visited[i] == 0:
    s.append(i)
    pos[i] = 0
  while len(s):
    p = s.pop()
    for q in e[p]:
      if pos[q[0]] == inf:
        pos[q[0]] = pos[p] + q[1]
        visited[q[0]] = 1
        s.append(q[0])
      else:
        if pos[q[0]] - pos[p] != q[1]:
          print("No")
          exit(0)
print("Yes")