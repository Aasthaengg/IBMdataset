import sys
import math

def str_input():
    S = raw_input()
    if S[len(S)-1] == "\r":
        return S[:len(S)-1]
    return S

p = [0, 0]

n = input()
for i in xrange(n):
    S = str_input().split()
    if S[0] < S[1]:
        p[1] += 3
    elif S[0] > S[1]:
        p[0] += 3
    else:
        p[0] += 1
        p[1] += 1

print p[0], p[1]