n, m, d = map(int, input().split())
if d > 0:
  print(max(0, 2 * (n - d) * (m - 1) / n / n))
else:
  print(max(0, (m - 1) / n))  