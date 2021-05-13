#-------------------------------------------------------------------------------
# coding: utf-8
# Created:     16/12/2015

import sys
io = sys.stdin

n = io.readline()

a0, a1 = [1, 1]
a2 = 1
for i in xrange(int(n)-1):
    a2 = a0 + a1
    a0, a1 = a1, a2

print a2