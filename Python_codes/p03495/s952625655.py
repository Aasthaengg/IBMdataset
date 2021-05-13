from collections import *
n,m=map(int,input().split())
l=list(map(int,input().split()))
k=len(set(l))
if(k<=m):
    print(0)
else:
    d=defaultdict(int)
    for i in l:
        d[i]+=1
    f=list(d.values())
    f.sort()
    g=k-m
    c=0
    for i in range(g):
        c+=f[i]
    print(c)
