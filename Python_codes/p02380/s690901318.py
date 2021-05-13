import sys
import math

def str_input():
    S = raw_input()
    if S[len(S)-1] == "\r":
        return S[:len(S)-1]
    return S

def float_to_str(num):
    return str("{:.10f}".format(num))

a, b, C = map(float, str_input().split())

h = b * math.sin(math.radians(C))
S = a * h / 2

dx = a - b * math.cos(math.radians(C))
dy = h

L = a + b + math.sqrt(dx*dx + dy*dy)

print float_to_str(S)
print float_to_str(L)
print float_to_str(h)