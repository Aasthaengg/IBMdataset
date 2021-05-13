N=int(input())
from collections import defaultdict
branch=defaultdict(set)
for i in range(N-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    branch[a]|={b}
    branch[b]|={a}
C=list(map(int,input().split()))
C.sort()
ans=[0]*N
used={0}
check={0}
M=sum(C[:-1])
while len(check)>0:
    now=check.pop()
    ans[now]=C.pop()
    for nex in branch[now]:
        if nex not in used:
            check|={nex}
            used|={nex}
print(M)
print(" ".join([str(x) for x in ans]))