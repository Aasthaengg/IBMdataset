import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

def check(i,s,s0):
    if i%2 == 0:
        if s == s0:
            return True
        else:
            return False
    else:
        if s != s0:
            return True
        else:
            return False

N = I()
print(0)
sys.stdout.flush()
s0 = str(input())
if s0 == 'Vacant':
    exit()

print(N-1)
sys.stdout.flush()
s1 = str(input())
if s1 == 'Vacant':
    exit()

ok = N-1
ng = 0
while True:
    mid = (ok+ng)//2
    print(mid)
    sys.stdout.flush()
    s = str(input())
    if s == 'Vacant':
        exit()
    flag = check(mid,s,s0)
    if flag:
        ng = mid
    else:
        ok = mid