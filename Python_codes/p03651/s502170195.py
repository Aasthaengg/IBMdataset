import fractions
from functools import reduce
N,K,*A = map(int,open(0).read().split())
g = reduce(fractions.gcd,A)
print("POSSIBLE" if K % g == 0 and K <= max(A) else "IMPOSSIBLE")  