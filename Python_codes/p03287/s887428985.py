from collections import defaultdict
from itertools import accumulate

N,M=map(int,input().split())
A=list(map(int,input().split()))

acc=list(accumulate(A))

d=defaultdict(int)

ans=0
for i in range(N):
    if acc[i]%M==0:
        d[acc[i]%M]+=1
        ans+=d[acc[i]%M]
    else:
        d[acc[i]%M]+=1
        ans+=d[acc[i]%M]-1
print(ans)