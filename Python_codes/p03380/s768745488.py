N=int(input())
*A,=map(int,input().split())
A.sort()
M=A[-1]
A=[-10**9]+A+[10**11]
from bisect import*
P=bisect_right(A,M/2)
if abs(A[P-1]-M/2)>abs(A[P]-M/2):
    m=A[P]
else:
    m=A[P-1]
print(M,m)