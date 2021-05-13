from collections import *
n=int(input())
l=list(map(int,input().split()))
d=defaultdict(int)
for i in l:
    d[i]+=1
c=0
for i in d:
    if(i!=d[i]):
        if(d[i]>i):
            c+=d[i]-i
        else:
            c+=d[i]
print(c)
