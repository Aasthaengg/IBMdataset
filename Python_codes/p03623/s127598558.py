x, a, b = map(int, input().split())

k = (x - a) ** 2
l = (x - b) ** 2

if k < l:
  print('A')
else:
  print('B')