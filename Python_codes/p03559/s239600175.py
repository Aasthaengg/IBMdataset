import bisect
import math
import sys
n=int(input())
ans=0
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
for i in b:
    aa=bisect.bisect_left(a,i)
    cc=len(c)-bisect.bisect_right(c,i)
    ans+=aa*cc
print(ans)
