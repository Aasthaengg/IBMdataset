from fractions import gcd
from functools import reduce

N, K = map(int, input().split())
A = list(map(int, input().split()))
G = reduce(gcd, A)
print("POSSIBLE" if K%G == 0 and K <= max(A) else "IMPOSSIBLE")