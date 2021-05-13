import math
a, b, h, m = map(int, input().split())
ang = abs(((360 * h / 12) + (0.5 * m)) - (360 * m / 60))
print(math.sqrt((a ** 2 + b ** 2) - (2*a*b*math.cos(math.radians(ang)))))
