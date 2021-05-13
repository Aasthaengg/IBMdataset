from itertools import accumulate
from collections import Counter

N,M=list(map(int,input().split()))
S=[0]+list(accumulate(map(int,input().split())))

modlst=[]

for s in S:
    modlst.append(s%M)

c=Counter(modlst)
ans=0

for v in c.values():
    ans+=v*(v-1)//2

print(ans)