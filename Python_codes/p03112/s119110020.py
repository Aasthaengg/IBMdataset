def near(x, X):
    i = bisect_left(X, x)
    if i == 0: return [X[i]-x]
    elif i == len(X): return [X[i-1]-x]
    else: return [X[i]-x, X[i-1]-x]
from bisect import *
A, B, Q = map(int, input().split())
S, T = [], []
for _ in range(A):
    S.append(int(input()))
for _ in range(B):
    T.append(int(input()))
for _ in range(Q):
    res = 1<<40
    x = int(input())
    for a in near(x,S):
        for b in near(x,T):
            res = min(abs(a)+abs(a-b), abs(b)+abs(b-a), res)
    print(res)