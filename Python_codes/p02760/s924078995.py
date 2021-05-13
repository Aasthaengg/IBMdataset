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
    bingo = [False]*9
    dic = dict()
    c = 0
    for _ in range(3):
        tmp = list(IL())
        for rep in tmp:
            dic[rep] = c
            c += 1
    n = I()
    for _ in range(n):
        b = I()
        idx = dic.get(b)
        if idx is None:
            continue
        bingo[idx] = True
    
    flag = False
    for i in range(0,3):
        for j in range(0,7,3):
            if not bingo[i+j]:
                break
        else:
            flag = True
    if flag:
        print('Yes')
        return
        
    for i in range(0,7,3):
        for j in range(0,3):
            if not bingo[i+j]:
                break
        else:
            flag = True
    if flag:
        print('Yes')
        return

    if (bingo[2] and bingo[4] and bingo[6]) or (bingo[0] and bingo[4] and bingo[8]):
        print('Yes')
    else:
        print('No')
    return

if __name__=='__main__':
    solve()