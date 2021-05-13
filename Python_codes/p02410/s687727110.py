import sys
import math

n, m = map(int, raw_input().split())
A = []
b = []

for i in xrange(n) :
    A.append(map(int, raw_input().split()))

for i in xrange(m) :
    b.append(input())

for i in xrange(n) :
    sm = 0
    for j in xrange(m) :
        sm += A[i][j] * b[j]
    print sm