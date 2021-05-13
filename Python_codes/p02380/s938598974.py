import math
s = input().split(" ")
a = round(float(s[0]),8)
b = round(float(s[1]),8)
c = round(float(s[2]),8)
d = round(math.sqrt(a**2 + b**2 - 2*a*b*(round(math.cos(math.radians(c)),8))),8)
L = a + b + d
S = round(b * a * (round(math.sin(math.radians(c)),8)) / 2, 8)
h = round(S * 2 / a, 8)
print(S)
print(L)
print(h)