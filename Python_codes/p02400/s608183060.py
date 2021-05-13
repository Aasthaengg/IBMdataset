# Python 3+
import sys
import math

#file = open("test.txt")
file = sys.stdin

r = float(file.readline())
l = 2*math.pi*r
s = math.pi*r*r

print("{0:.6f} {1:.6f}".format(s, l))