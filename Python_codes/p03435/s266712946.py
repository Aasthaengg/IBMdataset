c = [list(map(int, input().split())) for _ in range(3)]

d = []
for i in range(3):
  d.append([])
  for j, k in zip([0, 1, 2], [1, 2, 0]):
    d[i].append(c[i][j]-c[i][k])

if d[0] == d[1] == d[2]:
  print('Yes')
else:
  print('No')