jin,ter,q=map(int,input().split())
INF=10**19
jil,tel=[-INF]+[int(input()) for i in range(jin)]+[INF],[-INF]+[int(input()) for i in range(ter)]+[INF]
from bisect import bisect_right as bl
for _ in range(q):
    x=int(input())
    ans=INF
    b,d=bl(jil,x),bl(tel,x)
    for s in jil[b-1:b+1]:
        for t in tel[d-1:d+1]:
            ans=min(min(abs(x-s),abs(t-x))+abs(t-s),ans)
    print(ans)