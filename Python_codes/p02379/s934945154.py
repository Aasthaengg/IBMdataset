from math import sqrt
x1, y1, x2, y2 = [float(i) for i in input().split(" ")]
print("{:.8f}".format(sqrt( (x2 -x1) ** 2 + (y2 - y1) ** 2)))