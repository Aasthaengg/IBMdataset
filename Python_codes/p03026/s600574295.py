from collections import deque
N=int(input())
G=[[] for i in range(N)]
for i in range(N-1):
    a,b=map(int,input().split())
    a-=1;b-=1
    G[a].append(b)
    G[b].append(a)
j=0
for i in range(N):
    if len(G[i])>len(G[j]):
        j=i
c=sorted([int(i) for i in input().split()])
M=sum(c)-max(c)
d=[-1 for i in range(N)]
q=deque([j])
while(len(q)>0):
    r=q.popleft()
    d[r]=c.pop()
    for p in G[r]:
        if d[p]==-1:
            q.appendleft(p)
print(M)
print(" ".join([str(i) for i in d]))
