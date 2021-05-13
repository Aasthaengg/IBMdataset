import math
from bisect import *
n=int(input())
a=sorted(list(map(int,input().split())))
tmp=a[0]
ans=1
aa=1
for i in range(1,n):
    if tmp*2>=a[i]:
        tmp+=a[i]
        ans+=1
    else:
        tmp+=a[i]
        ans=1
print(ans)