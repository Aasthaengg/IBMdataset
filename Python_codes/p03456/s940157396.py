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
    c = int(a+b)
    r = int(math.sqrt(c))
    if r*r<c:
        print('No')
    else:
        print("Yes")
    return

if __name__=='__main__':
    a,b = SL()
    solve()