x, a, b = map(int, input().split())

d_a = abs(x-a)
d_b = abs(x-b)

if d_a < d_b:
  print('A')
else:
  print('B')
