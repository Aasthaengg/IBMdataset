import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

def main():
    n,k,c = inpm()
    s = list(input())
    circle = []
    for i in range(n):
        if s[i] == 'o':
            circle.append(i)
    pre = -c-10
    cnt = 0
    front = []
    for i in range(len(circle)):
        if pre+c < circle[i]:
            front.append(i)
            pre = circle[i]
            cnt += 1
            if cnt == k:
                break
    pre = n+c+10
    cnt = 0
    back = []
    for i in range(len(circle)-1,-1,-1):
        if pre-c > circle[i]:
            back.append(i)
            pre = circle[i]
            cnt += 1
            if cnt == k:
                break
    back.sort()
    for i in range(k):
        if back[i] == front[i]:
            print(circle[front[i]]+1)
    
if __name__ == "__main__":
    main()