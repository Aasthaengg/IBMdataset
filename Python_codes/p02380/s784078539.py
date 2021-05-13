import sys
import math

for line in sys.stdin:
    if len(line)>1:
        a, b, r = line.strip('\n').split()
        a, b, r = float(a), float(b), math.radians(float(r))
        
        h = b * math.sin(r)
        c = (a**2 + b**2 - 2*a*b*math.cos(r))**0.5
        l = a + b + c
        s = a * h / 2
        print s
        print l
        print h