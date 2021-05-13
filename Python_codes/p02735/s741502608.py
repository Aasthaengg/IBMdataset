from math import ceil,floor,comb,factorial,gcd,pow,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from copy import deepcopy
from time import time
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

def bfs():
    que = deque()
    que.append([0, 0])
    if s[0][0] == '#':
        d[0][0] = 1
    else:
        d[0][0] = 0

    while que:
        p = que.popleft()
        if p[0] == h-1 and p[1] == w-1:
            break

        for i in range(2):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if s[p[0]][p[1]] == '.' and  s[ny][nx] == '#':
                    if d[ny][nx] > d[p[0]][p[1]]+1:
                        d[ny][nx] = d[p[0]][p[1]]+1
                        que.append([ny, nx])
                else:
                    if d[ny][nx] > d[p[0]][p[1]]:
                        d[ny][nx] = d[p[0]][p[1]]
                        que.append([ny, nx])

    return d[h-1][w-1]

h, w = MAP()
s = [input() for i in range(h)]
d = [[inf]*w for i in range(h)]

dy = [1, 0]
dx = [0, 1]

print(bfs())