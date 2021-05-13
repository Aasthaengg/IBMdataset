n=int(input())
from bisect import bisect_left,bisect_right
s=list(input())
q=int(input())
D={chr(ord("a")+i):[] for i in range(26)}
for i ,j in enumerate(s):
    D[j].append(i)
ans=0
for i in range(q):
    x=list(input().split())
    if x[0]=="1":
        l=int(x[1])
        l-=1
        r=x[-1]
        if r==s[l]:
            continue
        rr=bisect_left(D[r],l)
        D[s[l]].remove(l)
        D[r].insert(rr,l)
        s[l]=r
    else:
        l=int(x[1])
        r=int(x[2])
        l-=1
        r-=1
        ans=0
        for i in range(26):
            W=chr(ord("a")+i)
            ll=bisect_left(D[W],l)
            rr=bisect_right(D[W],r)
            if rr-ll>0:
                ans+=1
        print(ans)

