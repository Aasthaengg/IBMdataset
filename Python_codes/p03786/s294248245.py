n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
from itertools import accumulate
a=list(accumulate(a))
ans=0
for i in range(n-1):
    if 2*a[i]>=a[i+1]-a[i]:
        ans+=1
    else:
        ans=0
print(ans+1)