import sys
readline = sys.stdin.readline

H,W = map(int,readline().split())
G = [None] * 10

for i in range(10):
  G[i] = list(map(int,readline().split()))

for k in range(10):
  for i in range(10):
    for j in range(10):
      if G[i][j] > G[i][k] + G[k][j]:
        G[i][j] = G[i][k] + G[k][j]

ans = 0
for i in range(H):
  line = list(map(int,readline().split()))
  for j in range(W):
    if line[j] == -1:
      continue
    if line[j] == 1:
      continue
    ans += G[line[j]][1]

print(ans)