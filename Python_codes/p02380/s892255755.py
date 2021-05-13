import math
a, b, C = map(float, input().split())
C = math.radians(C)
S = a * b * math.sin(C) * 0.5
c =(a**2 + b**2 - 2*a*b*math.cos(C))**0.5
L = a + b + c
h = b * math.sin(C)
result = [S, L, h]
for i in result:
    print(i)
