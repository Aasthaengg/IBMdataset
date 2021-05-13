import math

S = int(input())
t = math.sqrt(S)
a = b = math.ceil(t)

if a*(b-1) >= S:
  b -= 1

d = a*b - S
if d == 0:
  c = 0
else:
  c = 1
print("0 0 {} {} {} {}".format(a, c, d, b))