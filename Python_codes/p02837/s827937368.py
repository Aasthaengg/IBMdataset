import sys
import itertools
# import numpy as np
import time
import math
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())

people = [[-1 for _ in range(N)] for _ in range(N)]
for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        x -= 1
        people[i][x] = y

def countB(b):
    ret = 0
    while b > 0:
        if b % 2 == 1:
            ret += 1
        b //= 2

    return ret

ans = 0
for i in range(2 ** N):
    hs = [-1] * N
    contradiction = False
    for j in range(N):
        if i & 1 << j > 0:
            for k in range(N):
                if people[j][k] == -1:
                    continue
                if hs[k] == -1:
                    hs[k] = people[j][k]
                else:
                    if hs[k] != people[j][k]:
                        contradiction = True
    if not contradiction:
        for j in range(N):
            if hs[j] == -1:
                continue
            if i & 1 << j > 0 and hs[j]:
                continue
            if i & 1 << j == 0 and not hs[j]:
                continue
            else:
                break
        else:
            ans = max(ans, countB(i))
print(ans)
    


