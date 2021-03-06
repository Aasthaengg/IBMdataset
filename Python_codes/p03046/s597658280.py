import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

from collections import deque

M,K = LI()

if M == 0:
    if K == 0:
        print(0,0)
    else:
        print(-1)
    exit()

if M == 1:
    if K == 0:
        print(0,0,1,1)
    else:
        print(-1)
    exit()

if K >= 2**M:
    print(-1)
else:
    A = deque([K])
    for i in range(2**M):
        if i == K:
            continue
        else:
            A.appendleft(i)
            A.append(i)
    A.append(K)
    print(*A)