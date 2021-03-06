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

S = input()
T = 'keyence'
N = len(S)

i = 0
while i<7 and S[i]==T[i]:
    i += 1
j = 0
while j<7 and S[N-1-j]==T[6-j]:
    j += 1
judge(i+j>=7,['YES','NO'])