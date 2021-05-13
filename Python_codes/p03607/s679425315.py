from collections import *
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
d=defaultdict(int)
for i in l:
    d[i]+=1
c=0
for i in d:
    if(d[i]%2==1):
        c=c+1
print(c)
