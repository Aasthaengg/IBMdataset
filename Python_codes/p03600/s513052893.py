import sys
from copy import deepcopy as dc
input = sys.stdin.buffer.readline
N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]
d2 = dc(d)
for k in range(N):
  for i in range(N):
    for j in range(N):
      d2[i][j] = min(d2[i][k] + d2[k][j], d2[i][j])
f = 0
for i in range(N):
  for j in range(N):
    if d[i][j] != d2[i][j]:
      f = 1
if f:
  print(-1)
else:
  res = 0
  for i in range(N):
    for j in range(N):
      x = 1
      for k in range(N):
        if k != i and k != j:
          if d[i][j] == d[i][k] + d[k][j]: x = 0
      res += x * d[i][j]
          
  print(res // 2)