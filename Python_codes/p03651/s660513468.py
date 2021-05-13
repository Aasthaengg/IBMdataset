# A - Getting Difference
import fractions
from functools import reduce

N, K = map(int, input().split())
A = list(map(int, input().split()))

gcd = reduce(fractions.gcd, A) 

if max(A)>=K and K%gcd==0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')