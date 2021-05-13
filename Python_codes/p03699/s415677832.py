import sys
from sys import exit
from collections import deque
from bisect import bisect_left, bisect_right, insort_left, insort_right #func(リスト,値)
from heapq import heapify, heappop, heappush
from math import *

sys.setrecursionlimit(10**6)
INF = 10**20
MOD = 10**9+7

def mint():
    return map(int,input().split())
def lint():
    return map(int,input().split())
def judge(x, l=['Yes', 'No']):
    print(l[0] if x else l[1])
def lprint(l, sep='\n'):
    for x in l:
        print(x, end=sep)

N = int(input())
s = [0]*N
for i in range(N):
    s[i] = int(input())
    
if sum(s)%10!=0:
    print(sum(s))
else:
    l = [x for x in s if x%10!=0]
    tmp = min(l) if len(l) else sum(s)
    print(sum(s)-tmp)