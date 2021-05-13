from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


a, b, c, d = map(int, input().split())
e = lcm(c, d)
num_e = b // e - (a - 1) // e
num_c = b // c - (a - 1) // c
num_d = b // d - (a - 1) // d
num_can_div = num_c + num_d - num_e

print((b - a) - num_can_div + 1)
