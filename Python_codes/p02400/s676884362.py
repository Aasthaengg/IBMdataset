from sys import stdin
from math import pi

r = float(stdin.readline().rstrip())

s, cl = pi * r ** 2, 2 * pi * r

print("{:.6f} {:.6f}".format(s, cl))

