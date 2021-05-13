n,k=[int(j) for j in input().split()]
l=[[] for i in range(n)]

for i in range(n-1):
    a,b=[int(j)-1 for j in input().split()]
    l[a].append(b)
    l[b].append(a)

s=set([0])
ans=k
mod=10**9+7
from collections import deque
q=deque([(0,k-1)])
while q:
    x,y=q.popleft()
    j=0
    for i in l[x]:
        if i in s:
            continue
        s.add(i)
        if y-j<=0:
            print(0)
            exit()
        ans*=y-j
        ans=ans%mod
        q.append((i,k-2))
        j+=1
print(ans)

