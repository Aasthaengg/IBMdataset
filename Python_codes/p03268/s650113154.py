n, k = map(int, open(0).read().split())
if k % 2:
  print((n // k) ** 3)
else:
  print((n // k) ** 3 + ((n + k // 2) // k) ** 3)