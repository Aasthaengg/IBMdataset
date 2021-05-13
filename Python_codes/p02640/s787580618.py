x, y = list(map(int, input().split()))
b = (y - 2 * x) / 2

if y >= 2 * x and y % 2 == 0 and x - b >= 0:
  print('Yes')
else:
  print('No')
