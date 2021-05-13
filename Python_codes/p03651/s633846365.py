from fractions import gcd
from functools import reduce

N, K = map(int, input().split())
A = list(map(int, input().split()))

g = reduce(gcd, A)
print('IMPOSSIBLE' if K > max(A) or K % g else 'POSSIBLE')
