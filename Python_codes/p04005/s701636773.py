a, b, c = map(int, input().split())
if a*b*c % 2 == 0:
  print(0)
else:
  a, b, c = sorted([a, b, c])
  print(a*b)