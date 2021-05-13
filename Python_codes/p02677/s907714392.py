import math

a, b, h, m = map(int, input().split())

tha = (math.pi / 6)*h+(math.pi / 360)*m
thb = (math.pi / 30)*m
th = abs(tha-thb)

costh = math.cos(th)

c = (a**2 + b**2 - 2*a*b*costh)**(0.5)

print(c)