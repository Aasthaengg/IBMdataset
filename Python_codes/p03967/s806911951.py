#import pysnooper
#import os,re,sys,operator,math,heapq,string
#from collections import Counter,deque
#from operator import itemgetter
#from itertools import accumulate,combinations,groupby,combinations_with_replacement
from sys import stdin,setrecursionlimit
#from copy import deepcopy

setrecursionlimit(10**6)
input=stdin.readline

s=input().rstrip()
gu,pa=0,0
win,lose=0,0
for i in s:
    if i=="g":
        if pa+1<=gu:
            pa+=1
            win+=1
        else:
            gu+=1
    else:
        if pa+1<=gu:
            pa+=1
        else:
            gu+=1
            lose+=1
print(win-lose)