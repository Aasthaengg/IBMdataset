#import pysnooper
#import numpy
#import os,re,sys,operator
from collections import Counter,deque
#from operator import itemgetter
#from itertools import accumulate,combinations,groupby,combinations_with_replacement,permutations
from sys import stdin,setrecursionlimit
#from bisect import bisect_left
#from copy import deepcopy
#import heapq
#import math
#import string
#from time import time
#from functools import lru_cache
setrecursionlimit(10**6)
input=stdin.readline

n,k=map(int,input().split())
w=[int(input().rstrip()) for _ in range(n)]
l,r=0,10**9
while l<r:
    m=(l+r)//2
    loop=0
    ch=False
    for i in range(k):
        noww=0
        while loop<n:
            if noww+w[loop]<=m:
                noww+=w[loop]
                loop+=1
            else: break
        else:
            ch=True
    if ch: r=m
    else: l=m+1
    #print(m,l,r)
print(l)
