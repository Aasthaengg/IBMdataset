#import numpy as np

n,m=map(int,input().split())
a=[]
k=[]
for _ in range(n):
    b=list(map(int,input().split()))
    k.append(b[0])
    a.append(b[1:])
#print(k)
#print(a[1][0])

#c=np.zeros(m)
c=[0]*m
for i in range(n):
    for j in range(k[i]):
        d=a[i][j]
#        print(d)
        c[d-1]+=1

ans=0
for i in range(m):
    if c[i]==n:
        ans+=1
print(ans)
