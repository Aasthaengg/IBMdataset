import sys
input=sys.stdin.readline
n=int(input())

l=[[] for _ in range(n)]
ab=[]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    l[a].append(b)
    l[b].append(a)
    ab.append((a,b))

ans=[0]*n

from collections import deque

c=list(map(int,input().split()))
c.sort(reverse=True)
c=deque(c)
q=deque()
q.append([0])
while q:
    ll=q.popleft()
    for v in ll:
        if ans[v]!=0:
            continue
        ans[v]=c.popleft()
        q.append(l[v])

x=0
for a,b in ab:
    x+=min(ans[a],ans[b])

print(x)
print(*ans)
