import math
a, b, C = map(float, input().split())

S = a * b * math.sin(math.radians(C))/2
L = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(C)))
h = S * 2 / a

print("{0:04f}".format(S))
print("{0:04f}".format(L))
print("{0:04f}".format(h))