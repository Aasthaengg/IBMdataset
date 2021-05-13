import math
import numpy as np
n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
alice=0
bob=0
k=math.floor(n/2)
if (n%2)==0:
    for i in np.arange(1,k+1):
        alice+=a[2*i-2]
        bob+=a[2*i-1]
if (n%2)==1:
    for i in np.arange(1,k+1):
        alice+=a[2*i-2]
        bob+=a[2*i-1]
    alice+=a[n-1]  
print(alice-bob)