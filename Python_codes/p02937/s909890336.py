from itertools import *
from collections import *
from bisect import *
s=list(input())
t=input()
sets=set(s)
"""
a=len(s)*len(t)
maxcount=len(s)
for i in range(100):
    if maxcount<a:
        maxcount**=10
    else:
        break
"""

for T in t:
    if not T in sets:
        print(-1)
        exit()
N=len(s)
dic={}
for i in range(N):
    if not s[i] in dic:
        dic.update({s[i]:[i]})
    else:
        dic[s[i]].append(i)

count=0
prei=0
for i in range(len(t)):
    idx=bisect_left(dic[t[i]],prei)
    if idx<len(dic[t[i]]):
        prei=dic[t[i]][idx]+1
    else:
        prei=dic[t[i]][0]+1
        count+=N
    if i==len(t)-1:
        count+=prei



print(count)
