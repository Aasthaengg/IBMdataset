paths = [list(map(int, input().split())) for _ in range(3)]

link = [[0 for _ in range(4)] for _ in range(4)]
for path in paths:
  link[path[0]-1][path[1]-1] += 1
  link[path[1]-1][path[0]-1] += 1

ans = 'YES'
for i in range(4):
  tmp = 0
  for j in range(4):
    tmp += link[i][j]

  if tmp >= 3:
    ans = 'NO'

print(ans)