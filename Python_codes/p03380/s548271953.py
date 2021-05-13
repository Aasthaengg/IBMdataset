
from bisect import bisect_left,bisect

n=int(input())
a=list(map(int,input().split()))

a.sort()
ai=max(a)


#if ai%2==0:
#    ai2=ai//2+1
#else:
#    ai2=ai//2
ai2=ai/2

jj=bisect(a,ai2)

if jj+1<n:
    if abs(a[jj]-ai2)>abs(a[jj+1]-ai2):
        jj=jj+1
if jj-1>=0:
    if abs(a[jj]-ai2)>abs(a[jj-1]-ai2):
        jj=jj-1
    
if jj==n-1:
    jj=jj-1
    
aj=a[jj]

print(ai,aj)

