t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

v1, v2 = b1 - a1, b2 - a2
x1, x2 = t1 * v1, t2 * v2
if x1 + x2 == 0:
  print('infinity')
else:
  if x1 < 0:
    x1, x2 = [x1 * -1, x2 * -1]

  if x1 + x2 > 0:
    print(0)
  else:
    dx = abs(x1 + x2)
    c = (x1 // dx) * 2 + 1
    if x1 % dx == 0:
      c -= 1
    
    print(c)