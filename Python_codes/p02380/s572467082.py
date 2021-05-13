import math

a,b,C = map(int, input().split())

S = 1/2 * a * b * math.fabs(math.sin(C / 360 * 2 * math.pi))
c = math.sqrt( a **2 + b **2 - 2*a*b*math.cos(C/360 * 2 * math.pi))
L = a + b + c
h = 2* S / a

print('{0:.7f}'.format(S))
print('{0:.7f}'.format(L))
print('{0:.7f}'.format(h))