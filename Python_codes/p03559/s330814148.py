N=int(input())
*A,=map(int,input().split())
*B,=map(int,input().split())
*C,=map(int,input().split())

A.sort()
C.sort()
from bisect import*
ans=0
for b in B:
    x=bisect_left(A,b)
    y=N-bisect_right(C,b)
    ans+=x*y
print(ans)