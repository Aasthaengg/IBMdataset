s=list(input())
t=list(input())
ns=len(s)
nt=len(t)
t_set=list(set(t))
s_set=list(set(s))
for i in range(len(t_set)):
    if t_set[i] not in s_set:
        print(-1)
        exit()

from collections import defaultdict, deque
from bisect import bisect_right
ds=defaultdict(list)
for i in range(ns):
    ds[s[i]].append(i)

components=[0]*26
for i in range(26):
    components[i]=len(ds[chr(i+97)])
lt=[-1]*nt
ord('a')
last=-1
for i in range(nt):
    j=bisect_right(ds[t[i]],last)
    if j==components[ord(t[i])-97]:
        lt[i]=ds[t[i]][0]
    else:
        lt[i]=ds[t[i]][j]
    last=lt[i]

kuriage=0
for i in range(1,nt):
    if lt[i]<=lt[i-1]:
        kuriage+=1

print(kuriage*ns+lt[-1]+1)