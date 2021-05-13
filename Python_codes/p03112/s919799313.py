import bisect

A,B,Q=map(int,input().split())
S=[-10**18]+[int(input()) for _ in range(A)]+[10**18]
T=[-10**18]+[int(input()) for _ in range(B)]+[10**18]

for i in range(Q):
    x=int(input())
    b,d=bisect.bisect_right(S,x), bisect.bisect_right(T,x)
    ans=float("inf")
    for s in [S[b-1], S[b]]:
        for t in [T[d-1], T[d]]:
            d1,d2=abs(s-x)+abs(t-s), abs(t-x)+abs(s-t)
            ans=min(ans,d1,d2)
    print(ans)