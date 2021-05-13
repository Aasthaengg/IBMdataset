from functools import reduce
from fractions import gcd
N,K,*A=map(int, open(0).read().split())
g=reduce(gcd, A)
if (g==gcd(g,K) or K in A) and K<=max(A):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")