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

n,m=map(int,input().split())
u=[list(map(int,input().split())) for i in range(m)]
s,t=map(int,input().split())
dic=[[] for i in range(n+1)]
for i in range(m):
    a,b=u[i]
    dic[a].append(b)
# print(dic)
itta=[[0]*3 for i in range(n+1)]
d=deque([[s,0]])
itta[s][0]=1
itta[t][0]=2
while d:
    tmp=d.popleft()
    
    # print(tmp)

    p,cnt=tmp
    for i in dic[p]:
        if itta[i][(cnt+1)%3]==1:
            continue
        elif itta[i][(cnt+1)%3]==2:
            print((cnt+1)//3)
            quit()
        else:
            itta[i][(cnt+1)%3]=1
            d.append([i,cnt+1])
    # print(itta)
print(-1)