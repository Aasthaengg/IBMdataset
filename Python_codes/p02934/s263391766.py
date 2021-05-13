n = int(input())
a = list(map(int, input().split()))

import math
def lcm(x, y):
    return (x*y)//math.gcd(x, y)
if n >=2:
    ue = lcm(a[0], a[1])
    if n >= 3:
        for i in range(2, n):
            ue = lcm(ue, a[i])
else:
    ue = a[0]

shita = 0
if n >=2:
    for i in range(len(a)):
        shita += ue//a[i]
else:
    shita = n

ans = ue / shita
print(f"{ans:.6f}")
