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
    if n<2:
        print(n)
        return
    x = 2
    while x*2<=n:
        x *= 2
    print(x)
    return

if __name__=='__main__':
    n = I()
    solve()