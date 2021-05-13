h, w = map(int, input().split())
res = []
for i in range(h):
  c = list(map(str, input().split()))
  res.append(c)
  res.append(c)
  
for j in res:
  print(*j, sep='')