import numpy as np
n=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
N=np.zeros(n)
for i in range(n):
    N[i]=a1[i]+np.sum(a2)
    a2[i]=0
    if i!=n-1:
        a1[i+1]+=a1[i]
print(int(np.max(N)))