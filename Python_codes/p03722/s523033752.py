import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]

n,m=map(int,input().split())
abc=[list(map(int,input().split())) for i in range(m)]


#True : 負の経路が存在する
def find_negative_loop(n,w,es):
    #負の経路の検出
    #n:頂点数, w:辺の数, es[i]: [辺の始点,辺の終点,辺のコスト]
    d = [float("inf")] * n
    d[0] = 0 
    #この始点はどこでもよい
    for i in range(n-1):
        for j in range(w):
            e = es[j]
            if d[e[1]-1] > d[e[0]-1] - e[2]:
                d[e[1]-1] = d[e[0]-1] - e[2]
    neg=[False]*n
    for i in range(n):
        for j in range(w):
            e=es[j]
            if d[e[1]-1] > d[e[0]-1] - e[2]:
                d[e[1]-1] = d[e[0]-1] - e[2]
                neg[e[1]-1]=True
            if neg[e[0]-1]==True:
                neg[e[1]-1]=True
    return (d,neg)


#############################
ans=find_negative_loop(n,m,abc)
if ans[1][-1]==True:
    print("inf")
else:
    print(-ans[0][-1])