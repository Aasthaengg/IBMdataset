import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N = I()
    W = []
    fail = False
    seen = set()
    for i in range(N):
        w = S()
        if i == 0:
            pass
        else:
            if w[0] != prev[-1]:
                fail = True
            if w in seen:
                fail = True
        seen.add(w)
        prev = w

    if fail:
        print("No")
    else:
        print("Yes")


main()

