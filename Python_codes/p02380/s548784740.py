import math

a, b, x = map(float, input().split())
x = math.radians(x)
S = 0.5 * a * b * math.sin(x)
h = b * math.sin(x)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(x))
L = a + b + c
print(S)
print(L)
print(h)