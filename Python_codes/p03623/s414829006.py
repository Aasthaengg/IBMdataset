x, a, b = (int(i) for i in input().split())
da = abs(x-a)
db = abs(x-b)
if da < db:
  print('A')
else:
  print('B')