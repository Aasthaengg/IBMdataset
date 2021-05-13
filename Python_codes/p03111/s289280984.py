def examA():
    N = DI()/dec(7)
    ans = N
    print(N)
    return

def examB():
    ans = 0
    print(ans)
    return

def examC():
    N, A, B, C = LI()
    L = [I()for _ in range(N)]
    loop = (1<<(2*N))
    ans = inf
    for l in range(loop):
        cost = 0
        bamboo_A = 0
        bamboo_B = 0
        bamboo_C = 0
        for j in range(N):
            if l&(1<<(2*j))>0:
                if l&(1<<(2*j+1))>0:
                    cost += 10
                    bamboo_A += L[j]
                else:
                    cost += 10
                    bamboo_B += L[j]
            else:
                if l&(1<<(2*j+1))>0:
                    cost += 10
                    bamboo_C += L[j]
        if bamboo_A==0 or bamboo_B==0 or bamboo_C==0:
            continue
        cost += abs(A-bamboo_A) + abs(B-bamboo_B) + abs(C-bamboo_C) - 30
        ans = min(ans,cost)

    print(ans)
    return

def examD():
    N = I()
    P = LI()
    O_ = [-1]*N
    start = P[0]-1
    for i in range(N):
        O_[P[i]-1] = i
    #print(O_,start)
    A = [1]*N
    B = [1]*N
    for i in range(start+1,N):
        cur = O_[i]-O_[i-1]
        if cur>0:
            A[i] = A[i-1] + (cur+1)
            B[i] = B[i-1] - 1
        else:
            A[i] = A[i-1] + 1
            B[i] = B[i-1] - (-cur+1)
    for i in range(start)[::-1]:
        cur = O_[i]-O_[i+1]
        if cur>0:
            B[i] = B[i+1] + (cur+1)
            A[i] = A[i+1] - 1
        else:
            B[i] = B[i+1] + 1
            A[i] = A[i+1] - (-cur+1)
    if A[0]<1:
        add = (1-A[0])
        for i in range(N):
            A[i] += add
    if B[-1]<1:
        add = (1-B[-1])
        for i in range(N):
            B[i] += add

    print(" ".join(map(str,A)))
    print(" ".join(map(str,B)))
    return

def examE():
    return

def examF():
    ans = 0
    print(ans)
    return


from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examC()

"""
9
7 3 9 1 8 4 5 6 2
"""