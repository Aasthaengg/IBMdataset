from functools import reduce
from operator import add, mul

N = int(input())
A = [int(x) for x in input().split()]

numer = reduce(mul, A)
denom = reduce(add, [(numer // A[i]) for i in range(N)])

print(numer / denom)