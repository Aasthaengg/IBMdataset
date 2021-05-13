import math
a,b,C = map(float, input().split())
C = math.radians(C)
h = b * math.sin(C)
S = a * h * .5
L = a + b + math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C))
print("{0:.6f}\n{1:.6f}\n{2:.6f}".format(S,L,h))