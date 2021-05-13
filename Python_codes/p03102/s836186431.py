import numpy as np

n,m,c=map(int,input().split())
b=list(map(int,input().split()))
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)

b=np.array(b).reshape(m,1)
a=np.array(a)

ab=np.dot(a,b)

ans=0
for i in range(n):
    if ab[i]+c>0:
        ans+=1

print(ans)