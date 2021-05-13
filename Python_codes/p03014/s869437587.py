import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

h,w=mp()
s=["#"*(w+2)]
for i in range(h):
    s.append("#"+input()+"#")
s.append("#"*(w+2))
ans=[[0]*(w+2) for i in range(h+2)]

for i in range(h+2):
    ran=[]
    c=1
    for j in range(1,w+2):
        if s[i][j]==s[i][j-1]:
            c+=1
        else:
            ran.append(c)
            c=1
    ran.append(c)
    p=0
    for j in range(len(ran)):
        for k in range(ran[j]):
            if j%2==1:
                ans[i][p]+=ran[j]
            p+=1

for i in range(w+2):
    ran=[]
    c=1
    for j in range(1,h+2):
        if s[j][i]==s[j-1][i]:
            c+=1
        else:
            ran.append(c)
            c=1
    ran.append(c)
    p=0
    for j in range(len(ran)):
        for k in range(ran[j]):
            if j%2==1:
                ans[p][i]+=ran[j]
            p+=1
x=0
for i in range(h+2):
    for j in range(w+2):
        x=max(x,ans[i][j]-1)
print(x)