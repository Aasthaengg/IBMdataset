x, a, b = map(int, input().split())
distance_a = abs(a - x)
distance_b = abs(b - x)

if distance_a < distance_b:
  print('A')
else:
  print('B')