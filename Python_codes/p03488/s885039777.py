import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
mod=pow(10,9)+7

s=input()
x,y=map(int,input().split())
lst=[[],[]]
cnt=0
tmp=0
for i in range(len(s)):
    if s[i]=="F":
        tmp+=1
    else:
        if cnt==0:
            x-=tmp
        else:
            if tmp!=0:
                lst[cnt%2].append(tmp)
        tmp=0
        cnt+=1
if cnt==0:
    x-=tmp
elif tmp!=0:
    lst[cnt%2].append(tmp)

sumx=sum(lst[0])
sumy=sum(lst[1])
# print(x,sumx)
if sumx<x or x<-sumx:
    print("No")
    exit()
if sumy<y or y<-sumy:
    print("No")
    exit()
dpx=[[0]*(sumx*2+1) for i in range(len(lst[0])+1)]
dpy=[[0]*(sumy*2+1) for i in range(len(lst[1])+1)]
dpx[0][sumx]=1
dpy[0][sumy]=1

for i in range(len(lst[0])):
    for j in range(sumx*2+1):
        if dpx[i][j]!=0:
            dpx[i+1][j+lst[0][i]]+=1
            dpx[i+1][j-lst[0][i]]+=1

for i in range(len(lst[1])):
    for j in range(sumy*2+1):
        if dpy[i][j]!=0:
            dpy[i+1][j+lst[1][i]]+=1
            dpy[i+1][j-lst[1][i]]+=1

# print(dpx)
# print(dpy)
if dpx[len(lst[0])][sumx+x]!=0 and dpy[len(lst[1])][sumy+y]!=0:
    print("Yes")
else:
    print("No")