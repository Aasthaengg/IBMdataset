
import sys
from bisect import bisect_left,bisect,bisect_right

icase=0
if icase==0:
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    d=[]
    cb=[[0]*2 for i in range(m)]
    for i in range(m):
        bi,ci=map(int,input().split())
        cb[i]=[ci,bi]
elif icase==2:
    n,m=10,3
    a=[1, 4, 5, 5, 7, 8, 13, 33, 52, 100]
    cb=[[30, 4], [10, 3], [4, 1]]

a.sort()
cb.sort(reverse=True)
    
asum=0
isum=0
isumm=0
for i in range(m):
    isum+=cb[i][1]
    if isum>n:
        if a[n-1]<=cb[i][0]:
            asum+=cb[i][0]*(n-isumm)
            print(asum)
            sys.exit()
        else:
            ii=bisect_right(a,cb[i][0])
            asum+=cb[i][0]*(ii-isumm)
            asum+=sum(a[ii:])
            print(asum)
            sys.exit()
    if a[isum-1]<=cb[i][0]:
        asum+=cb[i][0]*cb[i][1]
        isumm=isum
        continue
    else:
        ii=bisect_right(a,cb[i][0])
        asum+=cb[i][0]*(ii-isumm)
        asum+=sum(a[ii:])
        print(asum)
        sys.exit()
    
asum+=sum(a[isum:])
        
print(asum)
