from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce
from fractions import gcd
import sys
def input(): return sys.stdin.readline().rstrip()
def I(): return int(input())
def Is(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def TIR(n): return [TI() for _ in range(n)]
def S(): return input()
def Ss(): return input().split()
def LS(): return list(input())
def SR(n): return [S() for _ in range(n)]
def SsR(n): return [Ss() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
sys.setrecursionlimit(10**6)
MOD = 10**9+7
INF = 10**18
# ----------------------------------------------------------- #

s = S()
t = S()
l = len(s)
S_Alphabet = [-1]*26
T_Alphabet = [-1]*26
# ord('a') = 97
for i in range(l):
    si = ord(s[i])-97
    ti = ord(t[i])-97
    if S_Alphabet[si] == -1:
        S_Alphabet[si] = ti
    else:
        if S_Alphabet[si] == ti:
            continue
        else:
            print("No")
            exit()
    if T_Alphabet[ti] == -1:
        T_Alphabet[ti] = si
    else:
        if T_Alphabet[ti] == si:
            continue
        else:
            print("No")
            exit()
else:
    print("Yes")
