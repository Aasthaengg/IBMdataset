import sys
readline = sys.stdin.readline

n,k = map(int, readline().split())

a = list(map(int,readline().split()))

import math
from functools import reduce
g = reduce(math.gcd, a)

if k <= max(a) and k % g == 0:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")