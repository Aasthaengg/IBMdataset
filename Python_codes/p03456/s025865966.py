from math import sqrt
a, b = input().split()

integer = int(a + b)
sqr_int = sqrt(integer)

if sqr_int.is_integer() == True:
  print("Yes")
else:
  print("No")

