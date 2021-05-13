a, b = map(int, input().split())
if (b - a) % 2 == 0:
  print(int(min([a, b]) + (max([a, b]) - min([a, b])) / 2))
else:
  print('IMPOSSIBLE')