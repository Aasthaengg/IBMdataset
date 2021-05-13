a,b,q = map(int, input().split())
inf=10**18
s=[-inf]+[int(input()) for _ in range(a)]+[inf]
t=[-inf]+[int(input()) for _ in range(b)]+[inf]
x=[int(input()) for _ in range(q)]
from bisect import bisect_left,bisect_right
for i in range(q):
    idx_s=bisect_right(s,x[i])
    idx_t=bisect_right(t,x[i])
    ans=inf
    for ss in [s[idx_s-1],s[idx_s]]:
        for tt in [t[idx_t-1],t[idx_t]]:
            d1,d2=abs(ss-x[i])+abs(ss-tt),abs(tt-x[i])+abs(tt-ss)
            ans=min(ans,d1,d2)
    print(ans)