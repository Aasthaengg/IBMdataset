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
    exclude = set()
    prime = set()
    for i in range(2,int(math.sqrt(x))+1):
        if i in exclude:
            continue
        prime.add(i)
        j = i+i
        while j<=math.sqrt(x):
            exclude.add(j)
            j += i
    
    current = x
    while True:
        for rep in prime:
            if current%rep==0:
                break
        else:
            print(current)
            return
        current += 1
    return

if __name__=='__main__':
    x = I()
    solve()