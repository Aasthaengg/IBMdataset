import numpy as np
n,m,x=map(int,input().split())
a=2**64
b=[np.array(list(map(int,input().split())),"i8")for i in range(n)]
for i in range(2**n):
    c=bin(i)[2:]
    c="0"*(n-len(c))+c
    l=np.zeros(m)
    q=0
    for j in range(n):
        if c[j]=="1":
            q+=b[j][0]
            l+=b[j][1:]
    if np.min(l)>=x:
        a=min(a,q)
if a==2**64:
    print(-1)
else:
    print(a)