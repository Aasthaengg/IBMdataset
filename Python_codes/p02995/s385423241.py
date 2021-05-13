import math
a, b, c, d = map(int, input().split())


def calc(x):
    global c, d
    l = c // math.gcd(c, d) * d
    return x - x // c - x // d + x // l


print(calc(b) - calc(a - 1))
