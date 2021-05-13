import math
a,b,C = map(int, input().split())
t = math.radians(C)
S = 0.5*a*b*math.sin(t)
L = a + b + math.sqrt((a**2)+(b**2)-(2*a*b*math.cos(t)))
h = b*math.sin(t)
print("{:.5f}\n{:.5f}\n{:.5f}".format(S,L,h))