N,M,P = map(int, input().split())
E = [[] for _ in range(N)]
E2 = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int, input().split())
    E[a-1].append((b-1, -c+P))
    E2[b-1].append(a-1)

used1 = [0]*N
used1[0] = 1
from collections import deque
q = deque()
q.append(0)
while q:
    u = q.pop()
    for e in E[u]:
        if used1[e[0]] == 1:
            continue
        used1[e[0]] = 1
        q.append(e[0])

used2 = [0]*N
used2[N-1] = 1
q.append(N-1)
while q:
    u = q.pop()
    for e in E2[u]:
        if used2[e] == 1:
            continue
        used2[e] = 1
        q.append(e)

L = [0]*N
for i in range(N):
    L[i] = used1[i] & used2[i]
        
def BellmanFord(E, N, source):
    inf = 10**12
    d = [inf for _ in range(N)]
    d[source] = 0
    
    for i in range(N):
        for j in range(N):
            for edge in E[j]:
                if d[edge[0]] > d[j] + edge[1]:
                    d[edge[0]] = d[j] + edge[1]
                    if i == N-1 and L[edge[0]]== 1:
                        return -1
    
    return d

d = BellmanFord(E, N, 0)
if d == -1:
    print(-1)
else:
    print(max(0, -d[-1]))