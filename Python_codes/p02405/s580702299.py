hs = []
ws = []
while True:
  h, w = (int(i) for i in input().split())
  if not h == 0 == w:
    hs.append(h)
    ws.append(w)
  else:
    break

for i in range(len(hs)):
  h = hs[i]
  w = ws[i]
  for height in range(1, h + 1):
    for width in range(1, w + 1):
      if height == 1 or height % 2 != 0:
        if width % 2 != 0:
          print('#',end='')
        else:
          print('.',end='')
      else:
        if width % 2 != 0:
          print('.',end='')
        else:
          print('#',end='')
    print('')
  print('')