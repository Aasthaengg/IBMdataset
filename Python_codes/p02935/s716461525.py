import sys
from collections import deque
import numpy as np
import math
sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

if __name__=='__main__':
    n = I()
    v = list(IL())
    v.sort(reverse=True)
    while 1<len(v):
        tmp = v.pop()+v.pop()
        v.append(tmp/2)
        v.sort(reverse=True)
    print(v.pop())
    exit()