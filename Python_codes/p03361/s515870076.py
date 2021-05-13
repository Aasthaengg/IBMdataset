import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

h,w=mp()
g=["."*(w+2)]
for i in range(h):
    g.append("."+input()+".")
g.append("."*(w+2))
v=[[1,0],[-1,0],[0,1],[0,-1]]
for i in range(1,h+1):
    for j in range(1,w+1):
        if g[i][j]=="#":
            c=True
            for x,y in v:
                if g[i+x][j+y]=="#":
                    c=False
            if c:
                print("No")
                exit()
print("Yes")