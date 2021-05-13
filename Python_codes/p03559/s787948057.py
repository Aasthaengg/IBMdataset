from bisect import bisect_left
from bisect import bisect_right

N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

A.sort()
B.sort()
C.sort()

ans=0
for i in range(N):
    idxa=bisect_left(A,B[i])
    idxc=bisect_right(C,B[i])
    ans+=idxa*(N-idxc)

print(ans)
