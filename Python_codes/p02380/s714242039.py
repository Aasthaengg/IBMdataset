import math
a, b, C = map(int, input().split())
C = C / 180 * math.pi
S = a * b * math.sin(C) / 2
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
print('{0}'.format(S))
print('{0}'.format(a + b + c))
print('{0}'.format(2 * S / a))