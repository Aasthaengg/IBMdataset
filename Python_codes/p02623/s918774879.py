n,m,k=map(int,input().split())
from itertools import accumulate
from bisect import bisect_right
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ac=[0]+list(accumulate(a))
bc=[0]+list(accumulate(b))
temp=0

for i in range(n+1):
    if ac[i]<=k:
        count=i
        count+=bisect_right(bc,k-ac[i])-1
        temp=max(temp,count)
print(temp)