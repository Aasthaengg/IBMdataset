N,M = list(map(int,input().split()))
AB = []
from collections import deque

for i in range(M):
    AB.append(list(map(int,input().split())))


out = 0
for remove in range(M):
    G = [[] for i in range(N)]
    for i in range(M):
        if i==remove:
            continue
        else:
            A,B=AB[i]
            G[A-1].append(B-1)
            G[B-1].append(A-1)
    s = 0
    visit = [0]*N
    que = deque([s])
    visit[s] = 1
    while que:
        v = que.popleft()
        for w in G[v]:
            if visit[w] == 1:
                continue
            visit[w] =  1
            que.append(w)
    if sum(visit)!=N:
        out+=1
print(out)