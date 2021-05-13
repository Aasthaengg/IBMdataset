from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,pprint,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

h,w,k = inpl()
s = [input() for i in range(h)]
res = [[0]*w for i in range(h)]
cnt = 0
bb = set()
for y in range(h):
    if s[y].count('#') == 0: 
        bb.add(y); continue
    fg = False
    for x in range(w):
        if s[y][x] == '.':
            if fg:
                res[y][x] = cnt
        else:
            fg = True
            cnt += 1
            res[y][x] = cnt
for y in range(h):
    if y in bb: continue
    for x in range(w)[::-1]:
        if res[y][x]: continue
        res[y][x] = res[y][x+1]

for x in range(w):
    for y in range(h-1):
        if not y+1 in bb: continue
        res[y+1][x] = res[y][x]

for x in range(w):
    for y in range(h-1)[::-1]:
        if not y in bb: continue
        res[y][x] = res[y+1][x]

for i in res:
    print(*i)