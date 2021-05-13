a, b, c = map(int, input().split())
d = a - b
e = c - d
if e < 0:
  print(0)
else:
  print(e)