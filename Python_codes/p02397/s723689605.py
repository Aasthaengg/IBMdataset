import sys
for i in sys.stdin:
  x, y = map(int, i.split())
  if (x, y) == (0, 0): break
  elif x <= y:
    print(x, y)
  else:
    print(y, x)