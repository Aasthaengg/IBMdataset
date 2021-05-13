from functools import reduce
def reduce_wrapper(func, *args):
    if len(args) == 1:
        return reduce(func, args[0])
    return reduce(func, args)

from fractions import gcd
def lcm(*args):
    return reduce_wrapper(lambda x, y: x*y // gcd(x, y), *args)

def xgcd(a, b):
    ''' return (g, x, y) such that a*x + b*y = g = gcd(a, b) '''
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def modinv(n):
    g, x, _ = xgcd(n, mod)
    if g != 1:
        raise ValueError('Modinv is not exist! arg={}'.format(n))
    return x % mod

mod = 10**9 + 7
n, *A = map(int, open(0).read().split())

l = lcm(A) % mod
s = 0
for a in A:
    s += l * modinv(a)
    s %= mod
print(s)