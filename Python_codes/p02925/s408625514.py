import sys
import itertools
import numpy as np

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
N = int(readline())
A = [[-1] + [int(x) - 1 for x in row.split()][::-1] for row in readlines()]

# A.append([-1])

def f(cand):
    cand1 = set()
    can_use = []
    for n in cand:
        if A[A[n][-1]][-1] == n:
            can_use.append(n)
    for n in can_use:
        A[n].pop()
        cand1.add(n)
        if A[n][-1] != -1:
            cand1.add(A[n][-1])
    return len(can_use), cand1

answer = 0
rest = N*(N-1)
cand = set(range(N))
while True:
    answer += 1
    x, cand = f(cand)
    if x == 0:
        answer = -1
        break
    rest -= x
    if rest == 0:
        break

print(answer)