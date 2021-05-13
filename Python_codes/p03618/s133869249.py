A=input()
N=len(A)
from collections import defaultdict
cnt=defaultdict(int)
ans=1+N*(N-1)//2
for a in A:
    ans-=cnt[a]
    cnt[a]+=1
print(ans)