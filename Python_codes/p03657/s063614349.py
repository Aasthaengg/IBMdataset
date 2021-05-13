A, B = map(int, input().split())

a = A % 3
b = B % 3

if a == b == 1 or a == b == 2:
  print('Impossible')
else:
  print('Possible')