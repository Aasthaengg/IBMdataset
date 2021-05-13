a, b, c = map(int, input().split())

res = c - a + b

if res <= 0:
  print(0)
else:
  print(res)
