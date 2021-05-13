import math

a, b, c, d = map(int, input().split())
a = a - 1

cd = c * d // math.gcd(c, d)

b_n = b // c + b // d - b // cd
a_n = a // c + a // d - a // cd
print((b - b_n) - (a - a_n))