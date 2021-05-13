#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict,Counter
import decimal
import re
#import bisect
#
#    d = m - k[i] - k[j]
#    if kk[bisect.bisect_right(kk,d) - 1] == d:
#
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#

import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())


h,w = readInts()
dist = [['0'] * w for _ in range(h)]
maze = [input() for _ in range(h)]
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def bfs(y,x):
    dist[y][x] = '#'
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not(0 <= nx < w and 0 <= ny < h):
            continue
        if maze[ny][nx] == '#':
            continue
        dist[ny][nx] = str(int(dist[ny][nx]) + 1)


for y in range(h):
    for x in range(w):
        if maze[y][x] == '#':
            bfs(y,x)
for i in range(h):
    print("".join(dist[i]),sep = '')
