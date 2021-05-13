import math

a, b, c, d = list(map(int, input().split()))

ac = (a-1) // c
ad = (a-1) // d
bc = b // c
bd = b // d
cd_lcm =  (c * d) // math.gcd(c, d)
acd_lcm = (a-1) // cd_lcm
bcd_lcm = b // cd_lcm

l = b - a + 1

print(l - (bc - ac) - (bd - ad) + (bcd_lcm - acd_lcm))
