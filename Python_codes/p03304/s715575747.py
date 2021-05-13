import sys
import random

def rd():
        return sys.stdin.readline().rstrip()

def rdi():
        return [ int(x) for x in rd().split() ]

n, m, d = rdi()

if n <= 2*d or d == 0:
        r = (m-1) / float(n)
else:
        r = (m-1) * (2 * n - 2 * d) / float(n * n)

print "%.32f" % r
