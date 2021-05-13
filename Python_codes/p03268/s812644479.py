#import pysnooper
#import os,re,sys,operator,math,heapq,string
#from collections import Counter,deque
#from operator import itemgetter
#from itertools import accumulate,combinations,groupby,combinations_with_replacement
from sys import stdin,setrecursionlimit
#from copy import deepcopy

setrecursionlimit(10**6)
input=stdin.readline

n,k=map(int,input().split())
a=(n//k)**3
if k%2==1:
    print(a)
else:
    b=((n+(k//2))//k)**3
    print(a+b)