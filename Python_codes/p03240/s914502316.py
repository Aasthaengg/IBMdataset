n = int(input())
info = []
for _ in range(n):
  x, y, h = map(int,input().split())
  info.append((x, y, h))

def check(cx, cy):
  H = None
  fin = []
  for i in info:
    x = i[0]
    y = i[1]
    h = i[2]
    if h != 0:
      tmpH = h + abs(x-cx) + abs(y-cy)
      if H:
        if H != tmpH:
          return 0
      else:
        H = tmpH
    else:
      fin.append((x, y, h))
  for f in fin:
    x = f[0]
    y = f[1]
    if H - abs(x-cx) -abs(y-cy) > 0:
      return 0
  return H
      

for cx in range(101):
  for cy in range(101):
    h = check(cx, cy)
    if h >= 1:
      print(cx)
      print(cy)
      print(h)
      break