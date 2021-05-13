# input = sys.stdin.readline
from bisect import *
from collections import *
from heapq import *
# import functools
# import itertools
# import math
N,C=map(int,input().split())
stc=[list(map(int,input().split())) for i in range(N)]
stc=sorted(stc,key=lambda x:x[0])
#print(stc)
rokugaki=[]
for s,t,c in stc:

    a=[i for i in range(len(rokugaki)) if rokugaki[i][1]==c]
    if not a:
        a=[i for i in range(len(rokugaki)) if rokugaki[i][0]<s]
    if a:
        rokugaki[a[0]]=[t,c]

    else:
        rokugaki.append([t,c])
    #print(rokugaki)

print(len(rokugaki))
