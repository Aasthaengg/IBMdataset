n, m = map(int, input().split())
n, m = min(n, m), max(n, m)
if n == 1:
  if m == 1:
    print(1)
  else:
    print(m - 2)
else:
  print((n - 2) * (m - 2))
