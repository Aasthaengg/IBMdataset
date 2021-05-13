a, b, c = map(int, input().split())

d = a - b

if c <= d:
  print(0)
elif c > d:
  print(c - d)