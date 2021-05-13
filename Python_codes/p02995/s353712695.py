from math import gcd as gcd
a, b, c, d = map(int,input().split())
#cでわれるもの
s = gcd(c, d)
p = c * d // s
divide_c = b // c - (a - 1) // c
divide_d = b // d - (a - 1) // d
divide_cd = b // p - (a - 1) // p
print(int(b - a + 1 - divide_c - divide_d + divide_cd))