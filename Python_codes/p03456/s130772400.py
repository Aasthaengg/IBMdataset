import math
v = int(input().replace(" ", ""))
if math.sqrt(v).is_integer():
  print("Yes")
else:
  print("No")