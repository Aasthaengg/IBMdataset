import math
S = int(input())

a = int(math.sqrt(S))
if S - a**2 > 0:
  a += 1
b = a**2 - S
c = 1
if b >= 10**8:
  s = int(math.sqrt(b))
  for i in range(s):
    if b % (s-i) == 0:
      b //= (s-i)
      c *= (s-i)
      break
print(0, 0, a, b, c, a)