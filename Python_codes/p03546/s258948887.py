H, W = map(int, input().split())
C = []
wall = []

for _ in range(10):
  C.append(list(map(int, input().split())))

for _ in range(H):
  wall += list(map(int, input().split()))

for k in range(10):
  for i in range(10):
    for j in range(10):
      C[i][j] = min(C[i][j], C[i][k]+C[k][j])

ans = 0
for x in wall:
  if x == -1:
    continue
  else:
    ans += C[x][1]

print(ans)