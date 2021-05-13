from collections import defaultdict
from collections import deque

N, K=map(int, input().split())
A=list(map(int, input().split()))
for i in range(N):
    A[i]-=1
s=[0 for _ in range(N+1)]
for i in range(N):
    s[i+1]=(s[i]+A[i])%K
d=defaultdict(int)
ans=0
q=deque()
for j in range(N+1):
    ans+=d[s[j]]
    d[s[j]]+=1
    q.append(s[j])
    if len(q)==K:
        d[q[0]]-=1
        q.popleft()
print(ans)