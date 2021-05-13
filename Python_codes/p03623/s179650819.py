x, A, B = map(int, input().split())

if abs(x - A) < abs(x - B):
  print('A')
else:
  print('B')