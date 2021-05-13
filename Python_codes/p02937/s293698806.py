import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))

sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

s = input()
t = input()

loop = 0
index = -1

# tの要素が全てsに含まれていないと無理
# 部分集合かどうかを判定
if not set(t) <= set(s):
    print(-1)
    exit()

dic = defaultdict(list)
t_set = set(t)

for i, c in enumerate(s):
    dic[c].append(i)

for i in range(len(t)):
    # tを最初から最後まで見る
    # tのi番目の文字がsで，何番目に出てくるかのリストの中で，indexをinsertできる場所をidxとする
    idx = bisect_left(dic[t[i]], index)
    
    if idx < len(dic[t[i]]):
        # 0 start -> 1 start by plus 1
        index = dic[t[i]][idx] + 1
    elif idx >= len(dic[t[i]]):# hitしなくなったら，文字列を足す，loopする
        loop += 1
        index = -1 # 最初から
        idx = bisect_left(dic[t[i]], index)
        index = dic[t[i]][idx] + 1
print(len(s) * loop + index) 
    

