from math import *
n,h=map(int,input().split())
a=[]
b=[]
for i in range(n):
    A,B=map(int,input().split())
    a.append(A)
    b.append(B)
aa=max(a)
b.sort(reverse=True)
ans=0
for i in range(n):
    if b[i]>aa:
        h-=b[i]
        ans+=1
        if h<=0:
            print(ans)
            exit()
print(ans+ceil(h/aa))