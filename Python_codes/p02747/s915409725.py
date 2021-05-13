import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import defaultdict
from bisect import *
mod = 10**9+7

S = input()[:-1]
for i in range(5):
    if 'hi' * (i+1) == S:
        print('Yes')
        exit()
print('No')
