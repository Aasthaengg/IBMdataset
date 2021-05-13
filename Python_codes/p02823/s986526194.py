import sys
n, a, b = map(int, sys.stdin.readline().split())
c = b - a
if c % 2:
  d = min(a - 1, n - b)
  e = 1
  f = (b - a - 1) // 2
  print(d + e + f)
else:
  print(c // 2)
