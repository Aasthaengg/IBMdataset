import sys
import math

S = raw_input()
if S[len(S)-1] == "\r":
    S = S[:len(S)-1]
S = S*2

T = raw_input()
if T[len(T)-1] == "\r":
    T = T[:len(T)-1]

if T in S:
    print "Yes"
else:
    print "No"