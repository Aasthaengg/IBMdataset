#!/usr/bin/env python3
import sys
try: from typing import Any, Union, List, Tuple, Dict
except ImportError: pass
def debug(*args): print(*args, file=sys.stderr)
def exit(): sys.exit(0)


N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))


T_ = []
A_ = []

T_.append(("=", T[0]))
for i in range(1, N):
    if T[i-1] == T[i]:
        T_.append(("<=", T[i]))
    else:
        T_.append(("=", T[i]))

for i in range(N-1):
    if A[i] == A[i+1]:
        A_.append(("<=", A[i]))
    else:
        A_.append(("=", A[i]))
A_.append(("=", A[N-1]))


count = 1
for i in range(N):
    t0, t1 = T_[i]
    a0, a1 = A_[i]
    if t0 == "=" and a0 == "=":
        if t1 == a1:
            continue
        else:
            print(0)
            exit()
    elif t0 == "=":
        if t1 > a1:
            print(0)
            exit()
        else:
            continue
    elif a0 == "=":
        if a1 > t1:
            print(0)
            exit()
        else:
            continue
    else:
        count = (count * min(t1, a1)) % (10**9+7)

print(count)
