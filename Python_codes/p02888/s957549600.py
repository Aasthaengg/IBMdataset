N=int(input())
L=list(map(int,input().split()))
from bisect import bisect_right as br
from bisect import bisect_left as bl

L.sort()

res=0
for i in range(N):
    for j in range(N):
        if not i<j:
            continue
        m=abs(L[i]-L[j])
        M=L[i]+L[j]
        r=bl(L,M)-br(L,m)
        if m<L[i]<M:
            r-=1
        if m<L[j]<M:
            r-=1
        res+=r
print(res//3)