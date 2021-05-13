import math

a, b, x = map(float, input().split())

tan = (2*((a**2)*b-x))/a**3

if x <= (a**3)*tan/2:
    tan = (a*(b**2))/(x*2)

deg = math.degrees(math.atan(tan))
print(deg)