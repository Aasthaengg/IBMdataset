import math
line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
degree = c
rad = math.radians(degree)
s = a * b * math.sin(rad) / 2
l = a + b + math.sqrt(pow(a,2) + pow(b,2) - 2 * a * b * math.cos(rad))
h = b * math.sin(rad)
print("{0:.8f}".format(s))
print("{0:.8f}".format(l))
print("{0:.8f}".format(h))