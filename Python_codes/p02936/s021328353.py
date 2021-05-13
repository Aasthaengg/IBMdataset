from collections import deque
N,Q=map(int,input().split())

T=[[]for _ in range(N)]
for i in range(N-1):
    a,b =map(int,input().split())
    T[a-1].append(b-1)
    T[b-1].append(a-1)

ans=[0]*N
for i in range(Q):
    p,x=map(int,input().split())
    ans[p-1] += x
    
q=deque([0])
visited=set()
while q:
    now =q.popleft()
    visited.add(now)
    for n in T[now]:
        if n not in visited:
            ans[n] += ans[now]
            q.append(n)
print(*ans)