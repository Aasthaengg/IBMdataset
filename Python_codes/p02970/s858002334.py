a, b = map(int, input().split())
if a % (b * 2 + 1) == 0:
  print(a // (b * 2 + 1))
else:
  print(a // (b * 2 + 1) + 1)