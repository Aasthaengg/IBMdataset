w, h, x, y = map(int, input().split())
s = w * h
dx, dy = w / 2, h / 2
if (x == dx) & (y == dy):
  print(s / 2, 1)
else:
  print(s / 2, 0)