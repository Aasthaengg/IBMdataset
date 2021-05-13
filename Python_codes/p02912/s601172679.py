from decimal import Decimal
from bisect import bisect
n,m=map(int,input().split())
lst=sorted(map(Decimal, input().split()))

while m>0:
    p=lst[-1]
    index=bisect(lst,p/2)
    for i in range(n-1,index-1,-1):
        if m>0:
            lst[i]=lst[i]/2
            m-=1
    lst=sorted(lst)
    if lst[-1]<1:
        break

ans=0
for i in lst:
    ans+=i//1
print(ans)