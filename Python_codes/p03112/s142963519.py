A,B,Q=map(int, input().split())
from bisect import bisect_left

S=[]
for i in range(A):
    s=int(input())
    S.append(s)
T=[]
for i in range(B):
    t=int(input())
    T.append(t)

for i in range(Q):
    x=int(input())
    sidx=bisect_left(S, x)
    tidx=bisect_left(T, x)
    if 0<=sidx<A and 0<=tidx<B:
        a1=max(S[sidx], T[tidx])-x
    else:
        a1=float("INF")
    if 0<=sidx-1<A and 0<=tidx-1<B:
        a2=max(x-S[sidx-1], x-T[tidx-1])
    else:
        a2=float("INF")
    if 0<=sidx<A and 0<=tidx-1<B:
        a3=S[sidx]-T[tidx-1]+min(S[sidx]-x, x-T[tidx-1])
    else:
        a3=float("INF")
    if 0<=sidx-1<A and 0<=tidx<B:
        a4=T[tidx]-S[sidx-1]+min(T[tidx]-x, x-S[sidx-1])
    else:
        a4=float("INF")
    #print(a1,a2,a3,a4)
    ans=min(a1,a2,a3,a4)
    print(ans)
