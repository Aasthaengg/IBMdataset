import sys
import collections
from math import ceil

ma = lambda : map(int,input().split())
ni = lambda : int(input())
def height(H,cy,cx,y,x):
    return max(H- abs(cy-y) - abs(cx-x),0)

n = ni()
hs = [[-1]*101 for i in range(101)]
nx,ny = -1,-1
ls = []
#E h >0?
for i in range(n):
    x,y,h = ma()
    hs[y][x] = h
    if h>0:
        nx,ny = x,y
    ls.append((y,x))

for cy in range(101):
    for cx in range(101):
        H = hs[ny][nx] + abs(cy-ny) + abs(cx-nx)
        for y,x in ls:
            if hs[y][x]!= height(H,cy,cx,y,x):
                break
        else:print(cx,cy,H)
