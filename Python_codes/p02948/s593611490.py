
import sys

icase=0
if icase==0:
    n,m=map(int,input().split())
    ab=[[] for i in range(m)]
    for i in range(n):
        ai,bi=map(int,input().split())
        if m-ai>=0:
            ab[m-ai].append(-bi)
elif icase==1:
    n,m=3,4
    ab=[[-3, -1], [], [-2], []]    
elif icase==2:
    n,m=5,3
    ab=[[], [-1, -3], [-2, -3, -4]]
elif icase==3:
    n,m=1,1
    ab=[[]]

from heapq import heappop,heappush

if len(ab)==0:
    print(0)
    sys.exit()

n=len(ab)
h=[]
asum=0
for i in range(m-1,-1,-1):
    if len(ab[i])>0:
        for abi in ab[i]:
            heappush(h,abi)
#    print(i,h,asum)
    if len(h)>0:
        asum+=heappop(h)

print(-asum)
    
