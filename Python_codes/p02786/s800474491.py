import sys
from collections import deque
#import numpy as np
import math
#sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def solve(val):
    if val<=1:
        return 1
    else:
        return 2*solve(val//2)+1

if __name__=='__main__':
    h = I()
    print(solve(h))