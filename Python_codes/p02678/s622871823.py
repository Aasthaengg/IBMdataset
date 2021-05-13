import sys
from collections import *

N,M=map(int,input().split())
adj=defaultdict(list)
for ln in sys.stdin:
    A,B=map(int,ln.split())
    A,B=A-1,B-1
    adj[A].append(B)
    adj[B].append(A)

a={0:0}
que=deque([0])
while que:
    u=que.popleft()
    for v in adj[u]:
        if v not in a:
            a[v]=u
            que.append(v)

if N-1-len(a)>0:
    print('No')
else:
    print('Yes')
    for i in range(1,N):
        print(a[i]+1)
