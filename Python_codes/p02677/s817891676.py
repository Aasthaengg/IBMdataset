import math

Pi = math.pi
a, b, h, m = map(int, input().split())

theta = abs((m/30) - (h/6 + m/360))*Pi
C = (a*math.sin(theta))**2 + (b-a*math.cos(theta))**2
c = math.sqrt(C)

print(c)