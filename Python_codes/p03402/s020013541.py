import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        for _ in range(num): return []
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list,zip(*read_all))

#################

A,B = II()

if A>=B:
    s = [['#']*100 for _ in range(100)]
    B -= 1
    for i in range(1,100,4):
        for j in range(1,80,4):
            if B == 0:
                break
            s[i-1][j-1] = s[i-1][j] = s[i-1][j+1] = '.'
            s[i][j-1] = s[i][j+1] = '.'
            s[i+1][j-1] = s[i+1][j] = s[i+1][j+1] = '.'
            B -= 1
            A -= 1
        else:
            continue
        break
    for j in range(81,100,2):
        for i in range(0,100,2):
            if A==0:
                break
            s[i][j] = '.'
            A -= 1
        else:
            continue
        break

else:
    s = [['.']*100 for _ in range(100)]
    A -= 1
    for i in range(1,100,4):
        for j in range(1,80,4):
            if A == 0:
                break
            s[i-1][j-1] = s[i-1][j] = s[i-1][j+1] = '#'
            s[i][j-1] = s[i][j+1] = '#'
            s[i+1][j-1] = s[i+1][j] = s[i+1][j+1] = '#'
            A -= 1
            B -= 1
        else:
            continue
        break
    for j in range(81,100,2):
        for i in range(0,100,2):
            if B==0:
                break
            s[i][j] = '#'
            B -= 1
        else:
            continue
        break

print(100,100)
for s0 in s:
    print(*s0, sep='')