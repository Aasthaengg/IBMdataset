import bisect
a,b,q=map(int,input().split())
S=[];T=[]
for _ in range(a):
    s=int(input())
    S.append(s)
for _ in range(b):
    t=int(input())
    T.append(t)
S.append(10**12)
T.append(10**12)

for _ in range(q):
    x=int(input())
    idx_s=bisect.bisect_left(S,x)
    idx_t=bisect.bisect_left(T,x)
    se=S[idx_s]
    sw=S[idx_s-1]
    te=T[idx_t]
    tw=T[idx_t-1]

    ans=float("inf")
    for ss in [se,sw]:
        for tt in [te,tw]:
            ans=min(ans,abs(ss-x)+abs(tt-ss),abs(tt-x)+abs(tt-ss))
    print(ans)