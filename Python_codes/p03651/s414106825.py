from fractions import gcd
from functools import reduce


N, K = map(int, input().split())
A = list(map(int, input().split()))
g = reduce(gcd, A)
if K <= max(A) and (g == 1 or K % g == 0):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
