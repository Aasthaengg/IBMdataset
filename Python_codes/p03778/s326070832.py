W, a, b = map(int, input().split())
if b >= a:
  d = b - (a + W)
else:
  d = a - (b + W)

if d >= 1:
  print(d)
else:
  print(0)