from itertools import*
import math
from collections import*
from heapq import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = float("inf")
mod = 10**9+7
from functools import reduce
import sys
sys.setrecursionlimit(10**7)

N = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))
max_T = max(T)
max_A = max(A)
if max_A != max_T:
    print(0)
    exit()
mt,ma = 0,0
ans = 1
for i in range(N):
    if T[i] == max_T:

        break
    else:
        if T[i] > mt:
            mt = T[i]
        else:
            ans *= mt
            ans %= mod
for j in range(N)[::-1]:
    if A[j] == max_A:
        break
    else:
        if A[j] > ma:
            ma = A[j]
        else:
            ans *= ma
            ans %= mod
if i == j:
    print(ans)
    exit()
elif j < i:
    print(0)
    exit()
else:
    ans *= pow(max_A,j-i-1,mod)
    ans %= mod
    print(ans)
