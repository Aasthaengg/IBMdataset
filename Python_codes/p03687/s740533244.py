import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = np.array(list(read().rstrip().decode()))

def f(S, a):
    S = S == a
    if not np.any(S):
        return len(S)
    for n in range(len(S)):
        if np.all(S):
            return n
        S = S[1:] | S[:-1]

x = min(f(S, a) for a in S)
print(x)