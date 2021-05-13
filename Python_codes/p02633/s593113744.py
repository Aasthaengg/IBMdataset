X = int(input())
if 360 % X == 0:
  ans = int(360 / X)
else:
  import math
  kaku = (360 * X) / math.gcd(360, X)
  ans = int(kaku / X)
print(ans)