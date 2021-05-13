import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import defaultdict
from bisect import *
mod = 10**9+7

S = input()
if S.count('x') >= 8:
    print('NO')
else:
    print('YES')
