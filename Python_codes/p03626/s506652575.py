import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy,bisect
from operator import itemgetter

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
nf = lambda: float(ns())
na = lambda: list(map(int, stdin.readline().split()))
nb = lambda: list(map(float, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N = ni()
S = [ns() for _ in range(2)]
ct = [0] * N
if S[0][0] == S[1][0]:
    ct[0] = 3
else:
    ct[0] = 6

for i in range(N-1):
    if S[0][i] == S[1][i]:
        if S[0][i+1] == S[1][i+1] and S[0][i] == S[0][i+1]:
            ct[i+1] = ct[i]
        else:
            ct[i+1] = (ct[i] * 2) % mod
    else:
        if S[0][i] != S[0][i+1] and S[1][i] != S[1][i+1] and S[0][i+1] != S[1][i+1]:
            ct[i+1] = (ct[i] * 3) % mod
        else:
            ct[i+1] = ct[i]
print(ct[N-1])


