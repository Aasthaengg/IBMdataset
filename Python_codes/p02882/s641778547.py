a, b, x = map(int, input().split())
from math import degrees, atan2
if x<=a**2*b/2:
    tanj = (x*2)/(b*a)
    print(90-degrees(atan2(tanj, b)))
else:
    x = a**2*b - x
    tanj = (x*2)/(a**2)
    print(degrees(atan2(tanj, a)))