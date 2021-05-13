from fractions import gcd

a, b = map(int, input().split())
g = gcd(a, b)
L = a * b // g
print(L)
