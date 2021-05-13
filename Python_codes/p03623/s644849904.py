x, a, b = input().split()
x = int(x)
a = int(a)
b = int(b)
if x > a:
  xa = x-a
else:
  xa = a-x
if x > b:
  xb = x-b
else:
  xb = b-x
if xa > xb:
  print("B")
else:
  print("A")