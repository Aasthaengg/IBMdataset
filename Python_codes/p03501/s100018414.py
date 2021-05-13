n, a, b = map(lambda x: int(x), input().split())

if n*a < b:
  print(n*a)
else:
  print(b)