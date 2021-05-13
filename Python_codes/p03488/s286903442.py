import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
# from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

s=input()
x,y=map(int,input().split())
tate,yoko=[],[]
kaisi=0
tmp=0
flag=1
for i in range(len(s)):
    if s[i]=="F":
        tmp+=1
    elif s[i]=="T":
        if kaisi==0:
            kaisi=1
            x-=tmp
        elif flag==0:
            flag=1
            yoko.append(tmp)
        else:
            flag=0
            tate.append(tmp)
        tmp=0


if kaisi==0:
    kaisi=1
    x-=tmp
elif flag==0:
    flag=1
    yoko.append(tmp)
else:
    flag=0
    tate.append(tmp)

# if sum(yoko)==0 and sum(tate)==0:
#     if x==0 and y==0:
#         print("Yes")
#     else:
#         print("No")
#     quit()
# # print(yoko,tate)

if abs(x)>sum(yoko) or abs(y)>sum(tate):
    print("No")
    quit()
yokolst=[[0]*(sum(yoko)*2+1) for i in range(len(yoko)+1)]
tatelst=[[0]*(sum(tate)*2+1) for i in range(len(tate)+1)]
yokolst[0][sum(yoko)]=1
tatelst[0][sum(tate)]=1
# print(yokolst)
# print(tatelst)
for i in range(len(tate)):
    for j in range(len(tatelst[0])):
        if tatelst[i][j]==1:
            tatelst[i+1][j+tate[i]]=1
            tatelst[i+1][j-tate[i]]=1


for i in range(len(yoko)):
    for j in range(len(yokolst[0])):
        if yokolst[i][j]==1:
            yokolst[i+1][j+yoko[i]]=1
            yokolst[i+1][j-yoko[i]]=1


# print(yokolst)
# print(tatelst)

if tatelst[-1][sum(tate)+y]==1 and yokolst[-1][sum(yoko)+x]==1:
    print("Yes")
else:
    print("No")