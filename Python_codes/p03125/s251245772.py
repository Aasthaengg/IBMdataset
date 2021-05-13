a, b = map(int, input().split())
large = max(a, b)
small = min(a, b)
if (large % small) == 0:
  print(a + b)
else:
  print(b - a)