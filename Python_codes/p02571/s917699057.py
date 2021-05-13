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
    lent = len(t)
    lens = len(s)
    ans = lent
    for i in range(lens-lent+1):
        tmp = 0
        for j in range(lent):
            if t[j] != s[j+i]:
                tmp += 1
        ans = min(ans,tmp)
    print(ans)
    return

if __name__=='__main__':
    s = S()
    t = S()
    solve()