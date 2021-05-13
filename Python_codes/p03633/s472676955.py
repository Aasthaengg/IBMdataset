from functools import reduce
n = int(input())
ts = [int(input())for _ in range(n)]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a*(b//gcd(a, b))


print(reduce(lcm, ts))
