import math
r = float(input())

S = r * r * math.pi
C = r * 2 * math.pi
print("{0:02.6f}".format(S), end =" ")
print("{0:02.6f}".format(C))