import numpy as np
from itertools import groupby

N = int(input())
T = np.array(['0'] + input().split() + ['10000000000'], np.int64)
A = np.array(['10000000000'] + input().split() + ['0'], np.int64)
mod = 10 ** 9 + 7

t = (T[1:] != T[:-1]) * T[1:]
a = (A[1:] != A[:-1]) * A[:-1]
t = t[:-1]
a = a[1:]

flag = True
idx = np.where((t != 0) & (a != 0))[0]
if np.any(t[idx] != a[idx]):
    flag = False

seq = np.maximum(t, a)
if np.any(seq > T[1:-1]) or np.any(seq > A[1:-1]):
    flag = False

if flag:
    group = [(i, len(list(j))) for i, j in groupby(seq.tolist())]
    answer = 1
    for i, (key, n) in enumerate(group):
        if key == 0:
            answer *= pow(min(group[i - 1][0], group[i + 1][0]), n, mod)
            answer %= mod
    print(answer)
else:
    print(0)
