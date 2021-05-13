N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
ans=0
from bisect import bisect_left,bisect_right
for i in B:
   ans+=(bisect_left(A,i))*(N-bisect_right(C,i))
print(ans)