n, m, d = map(int, input().split())

if d == 0:
  p = n / (n * n)
else:
  p = 2 * (n - d) / (n * n)

print(p * (m - 1))
