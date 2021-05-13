import bisect
from collections import Counter
from collections import defaultdict
s=input()
t=input()
#s="contest"
#t="antakuso"
sd=Counter(s)
td=Counter(t)
N=len(t)
Ns=len(s)
for ts in td:
    if ts not in sd:
        print(-1)
        exit()
D=defaultdict(list)
for i in range(Ns):
    D[s[i]].append(i)
ans=0
for i in range(N):
    if i==0:
        pre=min(D[t[i]])
    else:
        L=D[t[i]]
        idx=bisect.bisect(L,pre)
        if idx==len(L):
            ans+=Ns
            pre=min(L)
        else:
            pre=L[idx]
    if i==N-1:
        ans+=pre+1
print(ans)
