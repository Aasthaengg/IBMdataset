c = {}
for i in range(3):
  c[i] = list(map(int, input().split()))
tfc = 0
for i in range(101):
  if tfc == 3:
    break
  else:
    tfc = 0
  cx = []
  for j in c.values():
    for k in j:
      cx.append(k)
  if i > max(cx):
    break
  b = []
  for j in range(3):
    b.append(c.get(0)[j] - i)
  for j in range(3):
    p = []
    for k in range(3):
      p.append(c.get(j)[k] - b[k])
    if min(p) == max(p):
      tfc += 1
if tfc == 3:
  print('Yes')
else:
  print('No')