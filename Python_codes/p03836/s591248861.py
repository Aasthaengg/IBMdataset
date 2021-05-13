sx, sy, tx, ty = map(int, input().split())
xf, xb, yf, yb = 'R', 'L', 'U', 'D'
dx = abs(tx - sx)
dy = abs(ty - sy)

if tx < sx:
  xf, xb = 'L', 'R'
if ty < sy:
  yf, yb = 'D', 'U'

s = ""
if dx == 0:
  s += yf*dy
  s += xf
  s += yb*dy
  s += xb
  s += xb
  s += yf*dy
  s += xf
  s += yf
  s += xf*2
  s += yb*(dy+2)
  s += xb*2
  s *= yb
elif dy == 0:
  s += xf*dx
  s += yb
  s += xb*dx
  s += yf
  s += yf
  s += xf*dx
  s += yb
  s += xf
  s += yb*2
  s += xb(dx+2)
  s += yf*2
  s += xf
else:
  s += yf*dy
  s += xf*dx
  s += yb*dy
  s += xb*dx
  s += xb
  s += yf*(dy+1)
  s += xf*(dx+1)
  s += yb
  s += xf
  s += yb*(dy+1)
  s += xb*(dx+1)
  s += yf

print(s)