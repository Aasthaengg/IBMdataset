import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int,input().split())
G=[[] for _ in range(3*(n+1))]
for _ in range(m):
    u,v=map(int,input().split())
    G[3*u].append(3*v+2)
    G[3*u+1].append(3*v)
    G[3*u+2].append(3*v+1)
s,t=map(int,input().split())

Q=deque()
Q.append(s*3)
D=[-3 for _ in range(3*(n+1))]
D[s*3]=0

while Q:
    q=Q.popleft()
    for i in G[q]:
        if D[i]==-3:
            D[i]=D[q]+1
            Q.append(i)

print(D[t*3]//3)