import math
from numba import jit
n,k=map(int,input().split())
h=list(map(int,input().split()))
@jit
def a(N,K,H):
    s=[0]*n
    for i in range(1,N):
        total=math.inf
        for j in range(1,K+1):
            if i-j<0:
                break
            total=min(total,abs(H[i]-H[i-j])+s[i-j])
        s[i]=(total)
    print(s[-1])
a(n,k,h)