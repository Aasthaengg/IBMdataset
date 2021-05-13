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

cnt = 0

for i in xrange(n):
    m = input()
    for j in xrange(2, int(math.sqrt(m))+1):
        if m % j == 0:
            break
    else:
        cnt += 1

print cnt