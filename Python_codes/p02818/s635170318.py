a, b, k = map(int, input().split())

c = k - a
d = b - c

if c > 0:
  if d <= 0:
    print(0, 0)
  else:
    print(0, d)
else:
  print(a- k, b)