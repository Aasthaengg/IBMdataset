from math import ceil,floor,comb,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
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
    d = [[inf]*w for i in range(h)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
 
    que = deque([])
    que.append((sy, sx))
    d[sy][sx] = 0
    ret = 0
 
    while que:
        p = que.popleft()
        for i in range(4):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]
 
            if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] != '#' and d[ny][nx] == inf:
                que.append((ny,nx))
                d[ny][nx] = d[p[0]][p[1]] + 1
                ret = max(ret, d[ny][nx])
 
    return ret

h, w = MAP()
maze = [input() for i in range(h)]
ans = 0

for sy in range(h):
    for sx in range(w):
        if maze[sy][sx] == '#':
            continue
        else:
            ans = max(ans, bfs())

print(ans)