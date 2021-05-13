from math import gcd
a, b, c, d = map(int, input().split())
lcm = c*d//gcd(c, d)
cc = b//c - (a-1)//c
cd = b//d - (a-1)//d
clcm = b//lcm - (a-1)//lcm
print(b-a+1 - (cc + cd - clcm))