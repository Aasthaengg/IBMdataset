a, b = list(map(int, input().strip().split()))
c = a*b
if c%2 == 0:
  print('Even')
else:
  print('Odd')