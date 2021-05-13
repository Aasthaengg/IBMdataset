import math
pi = math.pi
rad = pi/180
a, b, C = map(float, input().split())
S = 0.5 * a * b * math.sin(C*rad)
L = a + b + math.sqrt(a**2 + b**2 -2*a*b*math.cos(C*rad))
h = abs(b*math.sin(C*rad))
print('{0:.5f}'.format(S))
print('{0:.5f}'.format(L))
print('{0:.5f}'.format(h))
