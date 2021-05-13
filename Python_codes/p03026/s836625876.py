from collections import deque
N=int(input())
AB=[tuple(map(int, input().split())) for _ in range(N-1)]
C=sorted(map(int, input().split()))
G=[[] for _ in range(N)]
for a,b in AB:
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
deq=deque(i for i in range(N) if len(G[i])==1)
D=[len(G[i]) for i in range(N)]
X=[0]*N
for c in C:
    i=deq.popleft()
    X[i]=c
    for j in G[i]:
        D[j]-=1
        if D[j]==1:
            deq.append(j)
ans=0
for a,b in AB:
    ans+=min(X[a-1],X[b-1])
print(ans)
print(*X)