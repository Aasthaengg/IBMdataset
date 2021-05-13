import sys
import math

n = input()

for x in xrange(1, n+1) :
    if x % 3 == 0 or str(x).find("3") != -1 :
        sys.stdout.write(" " + str(x))
print