a, b, x = map(int, input().split())
if a % x == 0:
  b -= b % x
  print((b - a)//x + 1)
else:
  a -= a % x
  b -= b % x
  print((b - a)//x)