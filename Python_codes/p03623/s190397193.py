x, a, b = map(int, raw_input().split())

if abs(a-x) > abs(b-x):
  print('B')
else:
  print('A')