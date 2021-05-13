from math import gcd


def lcm(x, y): return (x * y) // gcd(x, y)


def f(x): return (x // c) + (x // d) - (x // lcm(c, d)) - x


a, b, c, d = map(int, input().split())
print(f(a-1)-f(b))
