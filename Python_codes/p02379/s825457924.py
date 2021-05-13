import sys
import math

def str_input():
    S = raw_input()
    if S[len(S)-1] == "\r":
        return S[:len(S)-1]
    return S

def float_to_str(num):
    return str("{:.10f}".format(num))

x1, y1, x2, y2 = map(float, str_input().split())

dx = x2 - x1
dy = y2 - y1
print float_to_str(math.sqrt(dx*dx + dy*dy))