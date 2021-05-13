n, k = map(int, input().split())
from fractions import gcd
from functools import reduce
def gcd_list(xs):
    return reduce(gcd, xs)
ns = list(map(int, input().split()))
a = gcd_list(ns)
max_n = max(ns)
if k > max_n:
    print('IMPOSSIBLE')
elif k % a == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
