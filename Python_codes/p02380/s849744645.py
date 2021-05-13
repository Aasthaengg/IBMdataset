import math

a, b, c = map(float, input().split())
S =  0.5 * a * b * math.sin(c * math.pi / 180)
L = a + b + (a ** 2 + b ** 2 - 2 * a * b * math.cos(c * math.pi / 180)) ** 0.5
h = 2 * S / a

print("%f\n%f\n%f" % (S, L, h))