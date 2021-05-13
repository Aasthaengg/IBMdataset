import math
a, b, c, d = map(int, input().split())


def fn(n):
    lcm = (c * d) // math.gcd(c, d)
    return (n - (n // c) - (n // d) + (n // lcm))


print(fn(b)-fn(a-1))
