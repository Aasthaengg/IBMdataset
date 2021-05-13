from math import gcd

a, b, c, d = map(int, input().split())
a -= 1
lcm = c * d // gcd(c, d)
cnt_b = b - b // c - b // d + b // lcm
cnt_a = a - a // c - a // d + a // lcm
print(cnt_b - cnt_a)