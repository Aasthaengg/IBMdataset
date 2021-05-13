w, h, x, y, r = (int(i) for i in input().split())
if 0 + r <= x <= w - r and 0 + r <= y <= h - r:
  print('Yes')
else:
  print('No')