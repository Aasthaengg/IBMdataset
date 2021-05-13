import math
t1, t2, a1, a2, b1, b2 = [int(_) for _ in open(0).read().split()]
c1 = (b1 - a1) * t1
c2 = c1 + (b2 - a2) * t2
if c1 * c2 > 0:
    print(0)
    exit()
if c2 == 0:
    print('infinity')
    exit()
if c1 < 0:
    c1 *= -1
    c2 *= -1
ans = 2 * (c1 // (-c2)) + (c1 % c2 != 0)
print(ans)
