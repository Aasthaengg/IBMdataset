n,k=map(int,input().split())
xy=[]
for i in range(n):
    tmp=[int(j) for j in input().split()]
    xy.append((tmp[0],tmp[1]))
from operator import itemgetter
xy.sort(key=itemgetter(1))
xy.sort(key=itemgetter(0))
xy=tuple(xy)
l=tuple(enumerate(xy))
ans=10**100
for i,(a,b) in l[:n-k+1]:
    for j,(c,d) in l[i+k-1:]:
        l1=sorted(y for x,y in xy[i:j+1])
        l2=l1[k-1:]
        for p,q in zip(l1,l2):
            if p<=b and q>=d:
                ans=min(ans,(c-a)*(q-p))
print(ans)