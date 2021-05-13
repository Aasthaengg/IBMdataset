import math

def lcm(x, y):
    return x * y // math.gcd(x, y)

A, B, C, D = [int(_) for _ in input().split()]

a = A - 1
cd = lcm(C, D)
c = B // C - a // C
d = B // D - a // D
e = B // cd - a // cd

print(B - a - c - d + e)
