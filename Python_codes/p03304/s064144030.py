n, m, d = map(int, input().split())
if d >= n:
  print(0)
elif d == 0:
  print((n * (m - 1) * 10000000 / (n ** 2)) / 10000000)
else:
  print((2 * (n - d) * (m - 1) * 10000000 / (n ** 2)) / 10000000)
