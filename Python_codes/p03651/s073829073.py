from functools import reduce
from fractions import gcd

N, K, *X = map(int, open(0).read().split())

d = reduce(gcd, X)
for i in range(N):
    if X[i] < K:
        continue
        
    if (X[i] - K) % d == 0:
        print("POSSIBLE")
        break
else:
    print("IMPOSSIBLE")
