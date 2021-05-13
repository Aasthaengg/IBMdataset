import sys
from collections import deque,Counter
import numpy as np
import math
sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def Main():
    n = I()
    l = list(IL())
    m = max(l)
    s = sum(l)-m
    if m<s:
        print('Yes')
    else:
        print('No')
    return

if __name__=='__main__':
    Main()