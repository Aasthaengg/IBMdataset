g = [[] for _ in range(4)]
for _ in range(3):
  a, b = map(int, input().split())
  a, b = a-1, b-1
  g[a].append(b)
  g[b].append(a)
  
for i in range(4):
  if len(g[i]) != 1 and len(g[i]) != 2:
    print('NO')
    exit()
else:
  print('YES')