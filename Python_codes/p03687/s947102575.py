import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
eps = 1.0e-20
MOD = 10**9+7

def lcm(x,y):
    return x*y//gcd(x,y)
def mint():
    return map(int,input().split())
def lint():
    return list(map(int,input().split()))
def ilint():
    return int(input()), list(map(int,input().split()))
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)

s = input()
N = len(s)
ans = INF
for i in range(ord('a'),ord('z')+1):
    c = chr(i)
    k = 0
    tmp = 0
    for j in range(N):
        if s[N-1-j]==c:
            tmp = max(k,tmp)
            k = 0
        else:
            k += 1
    tmp = max(k,tmp)
    ans = min(ans,tmp)
print(ans)