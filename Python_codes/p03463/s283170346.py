n, a, b = map(int, input().split())
dist = b - a - 1
if dist % 2 == 1:
  print('Alice')
else:
  print('Borys')