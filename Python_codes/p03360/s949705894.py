#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
pri = lambda x: print(*x, sep='\n')

L = list(map(int, input().split()))
K = int(input())

L.sort()
val = L[0] + L[1] + L[2]*pow(2, K)
print(val)