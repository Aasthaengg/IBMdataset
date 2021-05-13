import sys
import math

r = float(sys.stdin.readline())
l = math.pi*r*2
s = math.pi*r**2
 
print("{:.6f} {:.6f}".format(s, l))