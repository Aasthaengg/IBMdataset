K = int(input())
A = tuple(map(int,input().split()))


lo = 2
hi = 3
for a in reversed(A):

    nl = (lo-1)//a+1
    nh = (hi-1)//a+1

    lo,hi = nl*a,nh*a

if lo < hi:
    print(lo,hi-1)
else:
    print(-1)