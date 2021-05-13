import collections
import sys
import math
N,T = map(int, input().split())
A = list(map(int, input().split()))
ans=0
for i in range(N-1):
    if A[i+1]-A[i]<T:
        ans+=A[i+1]-A[i]
    else:
        ans+=T
print(ans+T)