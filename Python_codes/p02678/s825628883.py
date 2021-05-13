import sys
from collections import *

N,M=map(int,input().split())
adj=[[] for _ in range(N+1)]
for ln in sys.stdin:
    A,B=map(int,ln.split())
    adj[A].append(B)
    adj[B].append(A)

ans=[0]*(N+1)
ans[1]=1
que=deque([1])
while que:
    A=que.popleft()
    for B in adj[A]:
        if ans[B]==0:
            ans[B]=A
            que.append(B)

print('Yes')
for i in range(2,N+1):
    print(ans[i])
