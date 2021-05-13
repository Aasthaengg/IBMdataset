import sys
from collections import deque
import numpy as np
import math
sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def solve():
    ans = 0
    for i,item in enumerate(x):
        a = item
        b = abs(item-k)
        ans += min(a,b)
    ans *= 2
    print(ans)
    return

if __name__=='__main__':
    n,k = I(),I()
    x = list(IL())
    solve()