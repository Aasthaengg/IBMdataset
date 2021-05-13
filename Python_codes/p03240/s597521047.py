N = int(input())
XYH = [list(map(int, input().split())) for _ in range(N)]
XYH.sort(key=lambda x:x[2], reverse=True)
isOk = False
cx = 0
while cx <= 100:
  cy = 0
  while cy <= 100:
    x, y, h = XYH[0]
    H = h+abs(x-cx)+abs(y-cy)
    i = 1
    isOk = True
    while i < N and isOk:
      x, y, h = XYH[i]
      if max(H-abs(x-cx)-abs(y-cy),0) != h:
        isOk = False
      i += 1
    if isOk:
      break
    cy += 1
  if isOk:
    break
  cx += 1
print(cx, cy, H)