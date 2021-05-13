import math
import functools

n,k = map(int, input().split())
a = list(map(int, input().split()))
g = functools.reduce(math.gcd, a)
if k % g == 0 and k <= max(a):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')