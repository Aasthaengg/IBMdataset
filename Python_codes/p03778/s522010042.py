w, a, b = map(int, input().split())
p, q = 0, 0
if a > b:
  p = a
  q = b
else:
  p = b
  q = a
if q + w > p:
  print(0)
else:
  print(p - q - w)
