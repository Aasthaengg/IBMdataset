from functools import reduce
from fractions import gcd

N, K, *X = map(int, open(0).read().split())

d = reduce(gcd, X)
if K % d == 0 and K <= max(X):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
