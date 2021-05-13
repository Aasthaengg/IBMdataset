import sys
from collections import deque
#import numpy as np
import math
#sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def solve():
    l = r = 0
    for i in range(0,x+1):
        if i in a:
            l += 1
    sign = 1 if x<n else -1
    for i in range(x,n+sign,sign):
        if i in a:
            r += 1
    ans = min(l,r)
    print(ans)
    return

if __name__=='__main__':
    n,m,x = IL()
    a = set(IL())
    solve()