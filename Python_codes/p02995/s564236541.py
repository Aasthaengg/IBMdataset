import math
a, b, c, d = map(int, input().split())
ac = (a - 1) // c
bc = b // c
ad = (a - 1) // d
bd = b // d
lcm = c * d // math.gcd(c,d)
acd = (a - 1) // lcm
bcd = b // lcm
print((b-a+1)-((bc-ac)+(bd-ad)-(bcd-acd)))