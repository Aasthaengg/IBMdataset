import fractions
from functools import reduce

N,K,*A = map(int,open(0).read().split())
g = reduce(fractions.gcd,A)
if max(A) < K:
    print("IMPOSSIBLE")
elif K % g == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE") 
