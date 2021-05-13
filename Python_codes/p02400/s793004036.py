import math
r = float(input())
t = r**2 * math.pi
s = 2 * r * math.pi
print(str("{0:.8f}".format(t)) + " " + str("{0:.8f}".format(s)))