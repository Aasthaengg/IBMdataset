import numpy as np
h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))

ans=[]
for i,j in enumerate(a):
    ans+=[(i+1)]*j
    
b=np.reshape(ans,(h,w))

for i,j in enumerate(b):
    if i%2==0:
        print(*j)
    else:
        print(*j[::-1])