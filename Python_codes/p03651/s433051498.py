from fractions import gcd
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)

N, K = map(int, input().split())
A =list(map(int, input().split()))

#if K <= max(A) and K % reduce(gcd, A) == 0:
if K <= max(A) and K % gcd_list(A) == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')