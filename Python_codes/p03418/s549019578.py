n, k = map(int, input().split())

if k == 0:
  print(n * n)
else:
  x = 0
  for b in range(k, n + 1):
    x += (n // b) * (b - k)
    r = n % b
    if r >= k:
      x += r - k + 1
  print(x)