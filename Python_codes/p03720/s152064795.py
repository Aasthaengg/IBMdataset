N, M = map(int, input().split())
load = {}
for i in range(N):
  load[i] = 0
for i in range(M):
  a, b = map(int, input().split())
  load[a-1] += 1
  load[b-1] += 1
for i in range(N):
  print(load[i])