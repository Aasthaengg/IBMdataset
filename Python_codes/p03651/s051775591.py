from math import gcd
from functools import reduce

_, k = map(int, input().split())
ar = list(map(int, input().split()))
mx = max(ar)
m = reduce(gcd, ar)
if k % m == 0 and k <= mx:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")