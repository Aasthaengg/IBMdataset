a, b = [int(i) for i in input().rstrip().split(' ')]
if a % 2 == 0 or b % 2 == 0:
  print('Even')
else:
  print('Odd')
