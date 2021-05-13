a, b = map(int, input().split())
c = 2*b
if a - c <= 0:
  print(0)
else:
  print(a - c)