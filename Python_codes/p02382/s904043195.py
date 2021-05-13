import sys
import math

def str_input():
    S = raw_input()
    if S[len(S)-1] == "\r":
        return S[:len(S)-1]
    return S

def float_to_str(num):
    return str("{:.10f}".format(num))

def list_input(tp):
    return map(tp, str_input().split())

# # # # # # # # # # # # # # # # # # # # # # # # #

n = input()
a = list_input(float)
b = list_input(float)

for d in xrange(1, 4):
    dist = 0
    for i in xrange(n):
        dist += pow(abs(a[i] - b[i]), d)
    dist = pow(dist, 1./d)
    print float_to_str(dist)

dist = 0
for i in xrange(n):
    dist = max(dist, abs(a[i] - b[i]))
print dist