d = {1:0, 2:0, 3:0, 4:0}
for i in range(3):
  a, b = map(int, input().split())
  d[a] += 1
  d[b] += 1
d = sorted(d.items(), key=lambda x:x[1])
if len(d) == 4 and d[0][1] == 1 and d[1][1] == 1 and d[2][1] == 2 and d[3][1] == 2:
  print('YES')
else:
  print('NO')