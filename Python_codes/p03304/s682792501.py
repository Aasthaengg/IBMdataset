n, m, d = list(map(int, input().split()))
if (d == 0):
  ans = (m - 1) * (1 / n)
  print(ans)
else:
  ans = (m - 1) * (2 * (n - d) / n ** 2)
  print(ans)
