def examA():
    S = I()
    X = [0,10**9,0]; Y = [0,1,0]
    X[2] = -S%(10**9)
    Y[2] = (S-1)//(10**9) +1
#    print(abs(X[1]*Y[2]-X[2]*Y[1]))
    print(X[0],Y[0],X[1],Y[1],X[2],Y[2])
    return

def examB():
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,inf
mod = 10**9 + 7
inf = 10**18

if __name__ == '__main__':
    examA()
