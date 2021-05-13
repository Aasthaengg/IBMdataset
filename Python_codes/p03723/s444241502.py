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
    global a,b,c
    st = {(a,b,c)}
    count = 0
    while a%2==0 and b%2==0 and c%2==0:
        ta = b//2 + c//2
        tb = a//2 + c//2
        tc = a//2 + b//2
        if (ta,tb,tc) in st:
            print(-1)
            return
        st.add((ta,tb,tc))
        a = ta
        b = tb
        c = tc
        count += 1
    print(count)
    return

if __name__=='__main__':
    a,b,c = IL()
    solve()