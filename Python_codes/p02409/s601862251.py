import sys
import math

n = input()
a = [[[0] * 10] * 3] * 4
a = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for i in xrange(n) :
    b, f, r, v = map(int, raw_input().split())

    a[b-1][f-1][r-1] += v;

for i in xrange(4) :
    for j in xrange(3) :
        for k in xrange(10) :
            sys.stdout.write(" " + str(a[i][j][k]))
        print
    if i < 3 :
        print "#" * 20