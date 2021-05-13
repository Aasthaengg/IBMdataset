# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    t1, t2 = a, b
    while True:
        if a%b:
            a, b = b, a%b
        else:
            break
    gcd = b
    lcm = t1/gcd*t2
    print "%d %d" %(gcd, lcm)