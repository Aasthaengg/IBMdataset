import math

a, b, x = map(int, input().split())
V = a **2 * b

if V / 2 <=  x:
    y = a ** 2 * b - x
    s = 2 * y / a ** 3

else:
    s = a * b ** 2 / (2 * x)

#print(s)
ans = math.atan(s)
ans = math.degrees(ans)

print(ans)