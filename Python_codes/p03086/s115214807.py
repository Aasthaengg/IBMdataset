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
    key = {"A","C","G","T"}
    mx = 0
    count = 0
    for item in s:
        if item in key:
            count += 1
        else:
            mx = max(mx,count)
            count = 0
    mx = max(mx,count)
    print(mx)
    return

if __name__=='__main__':
    s = S()
    solve()