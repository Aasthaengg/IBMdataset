import math

A, B, C, D = map(int, input().split())


def count(n, d):
    return n // d


c_dividable = count(B, C) - count(A-1, C)
d_dividable = count(B, D) - count(A-1, D)
cd = C*D // math.gcd(C, D)
cd_dividable = count(B, cd) - count(A-1, cd)

print((B-A+1) - (c_dividable+d_dividable-cd_dividable))
