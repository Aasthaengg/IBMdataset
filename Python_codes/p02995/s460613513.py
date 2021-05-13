from math import gcd
a, b, c, d = map(int, input().split())
lcm = c*d//gcd(c, d)
cc = b//c - (a//c - (a%c==0))
cd = b//d - (a//d - (a%d==0))
clcm = b//lcm - (a//lcm - (a%lcm==0))
print(b-a+1 - (cc + cd - clcm))
