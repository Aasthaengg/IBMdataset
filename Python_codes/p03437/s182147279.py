x, y = map(int, input().split())

if (x * y - x ) % y != 0:
  print(x * y - x)
else:
  print(-1)