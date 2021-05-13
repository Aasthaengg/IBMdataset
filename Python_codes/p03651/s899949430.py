N,K=map(int,input().split())
A=list(map(int,input().split()))
from fractions import gcd
g=A[0]
for i in A[1:]:
    g=gcd(g,i)
a=0
if A[0]%g!=K%g:
    a=1
if K>max(A):
    a=1
print(("IM" if a else "" )+"POSSIBLE")