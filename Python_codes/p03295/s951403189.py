#!/usr/bin/env python3
(n,m,),*b=[[*map(int,i.split())]for i in open(0)]
b=sorted(b,key=lambda x:x[1])
p=0
c=0
for i in b:
    if i[0]>=p:
        c+=1
        p=i[1]
print(c)
