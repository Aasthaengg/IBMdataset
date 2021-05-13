import math
a, b, k = list(map(int, input().split(' ')))
if k > a*a*b / 2:
    p = 2*b - 2*k / (a*a)
    q = (p**2 +a**2) ** 0.5
    limit = p
else:
    p = 2*k/(a*b)
    q = (p**2 +b**2) ** 0.5
    limit = b

left = 0.0
right = 90.0
while right > left + 1e-12:
    r = (left + right) / 2.0
    if q * math.sin(math.radians(r)) < limit:
        left = r
    else:
        right = r

print(r)