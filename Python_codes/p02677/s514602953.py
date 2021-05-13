import math

Pi = math.pi
a, b, h, m = map(int, input().split())

theta = abs((m/30) - (h/6 + m/360))*Pi
C =  a**2 + b**2 - 2*a*b*math.cos(theta)
c = math.sqrt(C)

print(c)