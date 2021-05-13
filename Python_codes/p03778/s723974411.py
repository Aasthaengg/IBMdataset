W, a, b = map(int, input().split())
if a > b:
  k = b
  b = a
  a = k
if a + W >= b:
  print(0)
else:
  print(b - (a + W))