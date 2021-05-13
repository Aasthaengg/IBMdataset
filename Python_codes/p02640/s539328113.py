x, y = [int(i) for i in input().split()]
if y % 2 == 0 and y <= x*4 and 2*x <= y:
  print('Yes')
else:
  print('No')