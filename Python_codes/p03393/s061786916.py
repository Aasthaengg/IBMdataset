import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

S = input()

alphas = [chr(ord('a') + i) for i in range(26)]

if len(S) < 26:
    remain = set(alphas) - set(S)
    remain = sorted(remain)
    print(S + remain[0])
else:
    pre = S[-1]
    i = 2
    while i < len(S):
        if pre < S[len(S) - i]:
            pre = S[len(S) - i]
            i += 1
        else:
            break
    if i == 26 and S[0] == 'z':
        print(-1)
        exit()
    front = S[:-i]
    back = sorted(S[-i:])
    to_be_changed = S[-i]
    for c in back:
        if c > to_be_changed:
            print(front + c)
            break






    

