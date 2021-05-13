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
T = input()

ls = len(S)
lt = len(T)
ans = []
for i in range(ls -lt, -1, -1):
    ss = list(S)
    ok = True
    for j in range(lt):
        if S[i + j] != '?' and S[i + j] != T[j]:
            ok = False
            break
        if S[i + j] == '?':
            ss[i + j] = T[j]
    if not ok:
        continue

    for j in range(ls):
        if ss[j] == '?':
            ss[j] = 'a'
    print("".join(ss))
    break
else:
    print("UNRESTORABLE")
