import math

a, b, x = map(int, input().split())

if x <= ((a**2) * b / 2):
    ans = a * (b**2) / (2 * x)
else:
    ans = 2 * ((a**2 * b) - x) / a**3
e = 90
s = 0
while e - s > 10**(-8):
    m = (e + s) / 2
    z = math.tan(math.radians(m))
    if z == ans:
        s = m
        break
    elif z > ans:
        e = m
    else:
        s = m
print(s)

