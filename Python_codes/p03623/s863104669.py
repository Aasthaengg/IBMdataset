X, a, b = [int(x) for x in input().split()]
da = abs(X-a)
db = abs(X-b)

if abs(X-a) < abs(X-b):
  print("A")
else:
  print("B")