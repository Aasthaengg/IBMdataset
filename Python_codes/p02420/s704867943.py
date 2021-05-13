import sys
import math

def str_input():
    S = raw_input()
    if S[len(S)-1] == "\r":
        return S[:len(S)-1]
    return S

while 1:
    S = str_input()

    if (S == "-"):
        break

    n = input()
    for i in xrange(n):
        x = input()
        S = S[x:] + S[:x]

    print S