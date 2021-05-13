def cnt(n):
    return n // c + n // d - n // e


from math import gcd

a, b, c, d = map(int, input().split())
e = c // gcd(c, d) * d
print(b - a + 1 - cnt(b) + cnt(a - 1))