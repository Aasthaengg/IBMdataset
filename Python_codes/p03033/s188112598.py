import bisect
import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
STX=[list(map(int,input().split())) for i in range(N)]
STX.sort(key=lambda x:x[2])
ans=[-1]*Q
jump=[-1]*Q
D=[int(input()) for i in range(Q)]
for s,t,x in STX:
    l=bisect.bisect_left(D,s-x)
    r=bisect.bisect_left(D,t-x)
    while(l<r):
        k=jump[l]
        if k==-1:
            ans[l]=x
            jump[l]=r
            l+=1
        else:
            l=k
for i in range(Q):
    print(ans[i])
