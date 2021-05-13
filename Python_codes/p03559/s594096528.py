import bisect

N=int(input())
A=[int(i) for i in input().split()]
A.sort()
B=[int(i) for i in input().split()]
B.sort()
C=[-int(i) for i in input().split()]
C.sort()
ans=0
for b in B:
    a=bisect.bisect_left(A,b)
    c=bisect.bisect_left(C,-b)
    # print(a,c)
    ans+=a*c
print(ans)