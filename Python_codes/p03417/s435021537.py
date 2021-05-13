n, m = map(int, input().split())
if n == 1 and m == 1:
  print(1)
  exit()
if n == 1 or m == 1:
  print(max(n, m) - 2)
  exit()
print((n - 2) * (m - 2))