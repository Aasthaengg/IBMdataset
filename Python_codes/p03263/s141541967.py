import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
fact = math.factorial
sys.setrecursionlimit(10**9)
INF = 10**9
mod = 10**9+7

H,W = I()
maze = []
for i in range(H):
    a = l()
    if i%2 == 1:
        a.reverse()
    for j in range(W):
        maze.append(a[j])
ans = []
zahyo = []
for i in range(H*W):
    b = i//W+1
    c = i%W+1
    if b%2 == 0:
        c = W-c+1
    zahyo.append([b,c])
for i in range(H*W-1):
    if maze[i]%2 == 1:
        ans.append(zahyo[i]+zahyo[i+1])
        maze[i+1] += 1
print(len(ans))
for s in ans:
    print(*s)