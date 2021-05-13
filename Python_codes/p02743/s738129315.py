import math
a, b, c = [int(i) for i in input().split(" ")]
d = c - a - b
if 0 < d and 4 * a * b < d * d:
  print("Yes")
else:
  print("No")