def examA():
    bit = 41
    N, K = LI()
    A = LI()
    B = [0]*bit
    for a in A:
        for j in range(bit):
            if a&(1<<j)>0:
                B[j] += 1
    ans = 0
    cnt = 0
    for i in range(bit)[::-1]:
        if N-B[i]<=B[i]:
            ans += (1 << i) * B[i]
        else:
            if cnt+(1<<i)>K:
                ans += (1 << i) * B[i]
            else:
                cnt += (1 << i)
                ans += (1 << i) * (N-B[i])
    print(ans)
    return

def examB():
    ans = 0
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examA()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""