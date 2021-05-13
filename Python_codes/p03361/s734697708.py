ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

h,w = nm()
s = []
for y in range(h):
  s.append([_ for _ in input()])

for y in range(h):
  for x in range(w):
    xx = [1,0,-1,0]
    yy = [0,1,0,-1]

    if s[y][x]=='.':
      continue

    ok = False
    for i in range(4):
      nx = x + xx[i]
      ny = y + yy[i]

      if 0 <= nx < w and 0 <= ny < h:
        if s[ny][nx]=='#':
          ok = True
    if not ok:
      print('No')
      exit()
print('Yes')

