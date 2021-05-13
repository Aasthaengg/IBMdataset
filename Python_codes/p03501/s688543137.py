n, a, b = list(map(int, input().split()))

p1 = a * n

if p1 < b:
  print(p1)
else:
  print(b)
