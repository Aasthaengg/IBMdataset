import sys
import math

def str_input():
    S = raw_input()
    if S[len(S)-1] == "\r":
        return S[:len(S)-1]
    return S

S = str_input()
n = input()

for i in xrange(n):
    arg = str_input().split()

    arg[1] = int(arg[1]);
    arg[2] = int(arg[2]);

    if arg[0] == "print":
        print S[arg[1]:arg[2]+1]
    elif arg[0] == "reverse":
        S = S[:arg[1]] + S[arg[1]:arg[2]+1][::-1] + S[arg[2]+1:]
    elif arg[0] == "replace":
        S = S[:arg[1]] + arg[3] + S[arg[2]+1:]