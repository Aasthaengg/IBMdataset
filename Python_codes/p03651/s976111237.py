N,K,*A=map(int,open(0).read().split())
from math import*
c=A[0]
for a in A:
    c=gcd(c,a)
print('IM'*(K%c>0 or K>max(A))+'POSSIBLE')