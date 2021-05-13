import math

a, b = map(str, input().split())
x = int(a + b)

if math.sqrt(x).is_integer():
  print("Yes")
else:
  print("No")
