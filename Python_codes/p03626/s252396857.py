#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter
#from scipy.misc import comb

MOD = 10**9+7

N = int(input())
S = []
for _ in range(2):
    s = input()
    S.append(s)

i = 0
if S[0][i] == S[1][i]:
    ans = 3
    i += 1
else:
    ans = 6
    i += 2

while i < N:
    if S[0][i] == S[1][i]:
        if S[0][i-1] == S[1][i-1]: ans *= 2
        else: ans *= 1
        ans %= MOD
        i += 1
    else:
        if S[0][i-1] == S[1][i-1]: ans *= 2
        else: ans *= 3
        ans %= MOD
        i += 2

print(ans)        