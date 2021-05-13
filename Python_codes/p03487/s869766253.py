N=int(input())
*A,=map(int,input().split())

from collections import*
C=Counter(A)
ans=0
for k,v in zip(C.keys(),C.values()):
    if k<=v:
        ans+=v-k
    else:
        ans+=v

print(ans)