#119_D
A,B,Q=map(int,input().split())
INF=10**15
S=[-INF]+[int(input()) for _ in range(A)]+[INF]
T=[-INF]+[int(input()) for _ in range(B)]+[INF]

from bisect import bisect_left

for _ in range(Q):
    x=int(input())
    s=bisect_left(S,x)
    t=bisect_left(T,x)
    
    sr=abs(S[s]-x)
    sl=abs(S[s-1]-x)
    tr=abs(T[t]-x)
    tl=abs(T[t-1]-x)
    
    Ans=min(max(sr,tr),max(sl,tl),2*sr+tl,sr+2*tl,2*tr+sl,tr+2*sl)
    
    print(Ans)