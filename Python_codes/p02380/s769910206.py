import math

a, b, C = list(map(int, input().split()))
C = math.radians(C)
S = 0.5 * a * b * math.sin(C)
l = a + b + math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C))
h = b * math.sin(C)
print("{:.5f}".format(S))
print("{:.5f}".format(l))
print("{:.5f}".format(h))