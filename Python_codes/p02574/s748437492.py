from functools import reduce
from math import gcd

N, *A = map(int, open(0).read().split())

C = [0] * (max(A) + 1)
for a in A:
    C[a] += 1

if reduce(gcd, A) != 1:
    print("not coprime")

elif all(sum(C[i::i]) <= 1 for i in range(2, len(C))):
    print("pairwise coprime")

else:
    print("setwise coprime")