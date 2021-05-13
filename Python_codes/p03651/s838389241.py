from math import gcd
from functools import reduce
n, k = map(int, input().split())
A = list(map(int, input().split()))
if k<=max(A) and k%reduce(gcd, A)==0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')