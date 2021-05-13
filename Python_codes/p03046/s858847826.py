from itertools import*
from math import*
from collections import*
from heapq import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = 10**18
mod = 10**9+7
from functools import reduce
import sys
sys.setrecursionlimit(10**7)

M,K = map(int,input().split())

if K == 0:
    print(*[i//2 for i in range(2**(M+1))])
elif M == 1:
    print(-1)
elif K < 2**M:
    X = [i for i in range(2**M) if i != K]
    print(*(X+[K]+X[::-1]+[K]))
else:
    print(-1)