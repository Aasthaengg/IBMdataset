_ = input()
A = [*map(int, input().split())]
C = [0] * (1000001)
for a in A: C[a] += 1
from functools import reduce
from math import gcd
t = any(sum(C[i::i]) > 1 for i in range(2, 1000001))
t += reduce(gcd, A) > 1
print(['pairwise','setwise','not'][t], 'coprime')
