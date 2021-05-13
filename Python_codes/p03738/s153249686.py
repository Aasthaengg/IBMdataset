import math
a = math.log(int(input()))
b = math.log(int(input()))
if a > b:
  print("GREATER")
elif a < b:
  print("LESS")
else:
  print("EQUAL")