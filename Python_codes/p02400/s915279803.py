import sys
import math

value = float(sys.stdin.readline())

print "%.9f %.9f" % (math.pi * value * value, 2.0 * math.pi * value)