import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
# 頻度 counter
S = [_S() for _ in range(N)]
c = collections.Counter(S)

judge = ['AC', 'WA', 'TLE', 'RE']
for j in judge:
    print(j + ' x ' + str(c[j]))