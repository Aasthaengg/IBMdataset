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

n,a,b,c,d=map(int,input().split())
s=input()
for i in range(b-1,d-1):
    if s[i]=="#" and s[i+1]=="#":
        print("No")
        quit()

if c<d:
    for i in range(a-1,c-1):
        # print(s[i],s[i+1])
        if s[i]=="#" and s[i+1]=="#":
            print("No")
            quit()

else:
    flag=0
    for i in range(b-2,d-1):
        # print(s[i],s[i+1],s[i+2])
        if s[i]=="." and s[i+1]=="." and s[i+2]==".":
            flag=1
    if flag==0:
        print("No")
        quit()
    for i in range(a-1,c-1):
        if s[i]=="#" and s[i+1]=="#":
            print("No")
            quit()
print("Yes")