#import pysnooper
#import os,re,sys,operator,math,heapq,string
#from collections import Counter,deque
#from operator import itemgetter
#from itertools import accumulate,combinations,groupby,combinations_with_replacement
from sys import stdin,setrecursionlimit
#from copy import deepcopy
setrecursionlimit(10**6)

#@pysnooper.snoop()
def dfs(v,s):
    seen[v]=True
    first[v]=s
    s+=1
    #print(v,g[v])
    for i in g[v]:
        if seen[i]:
            continue
        s=dfs(i,s)
    #print(s)
    last[v]=s
    return s+1

n=int(stdin.readline().rstrip())
seen=[False]*n
first=[0]*n
last=[0]*n
g=[[] for _ in range(n)]
s=1
for i in range(n):
    v=list(map(int,stdin.readline().rstrip().split()))
    for j in v[2:]:
        g[v[0]-1].append(j-1)
for i in range(n):
    if not seen[i]:
        s=dfs(i,s)
for i in range(n):
    print(i+1,first[i],last[i])
