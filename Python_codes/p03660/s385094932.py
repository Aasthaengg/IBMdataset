n=int(input())
G=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

from collections import deque
dist_f=[-1]*n
dist_f[0]=0
q=deque()
q.append(0)
while q:
    cur=q.popleft()
    for nx in G[cur]:
        if dist_f[nx]==-1:
            dist_f[nx]=dist_f[cur]+1
            q.append(nx)

dist_s=[-1]*n
dist_s[n-1]=0
q=deque()
q.append(n-1)
while q:
    cur=q.popleft()
    for nx in G[cur]:
        if dist_s[nx]==-1:
            dist_s[nx]=dist_s[cur]+1
            q.append(nx)
fenec,sunuke=0,0
for i in range(n):
    if dist_f[i]<=dist_s[i]:
        fenec+=1
    else:
        sunuke+=1
print("Fennec") if fenec>sunuke else print("Snuke")