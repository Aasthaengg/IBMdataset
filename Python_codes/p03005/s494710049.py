#import pysnooper
import os,re,sys,operator,math,heapq,string
#from collections import Counter,deque
#from operator import itemgetter
from itertools import accumulate,combinations#,groupby,combinations_with_replacement
from sys import stdin,setrecursionlimit
#from copy import deepcopy

setrecursionlimit(10**6)
input=stdin.readline

n,k=map(int,input().split())
print(n%k if n>=k else 0)