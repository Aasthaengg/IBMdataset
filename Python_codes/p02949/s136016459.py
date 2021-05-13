from collections import deque

N,M,P = map(int, input().split())
E = [[] for _ in range(N)]
Ei = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int, input().split())
    E[a-1].append((b-1, -c+P))
    Ei[b-1].append(a-1)
    
q = deque()
q.append(0)
used = [0]*N
used[0] = 1
while q:
    t = q.pop()
    for e in E[t]:
        if used[e[0]] == 1:
            continue
        used[e[0]] = 1
        q.append(e[0])
        
q.append(N-1)
used2 = [0]*N
used2[N-1] = 1
while q:
    t = q.pop()
    for e in Ei[t]:
        if used2[e] == 1:
            continue
        used2[e] = 1
        q.append(e)
        
L = [0]*N
for i in range(N):
    if used[i] == 1 and used2[i] == 1:
        L[i] = 1
    
def BellmanFord(E, N, source):
    inf = 10**10
    d = [inf for _ in range(N)]
    d[source] = 0
    for i in range(N):
        for j in range(N):
            e = E[j]
            if len(e) == 0:
                continue
            for edge in e:
                if d[edge[0]] > d[j]+edge[1]:
                    d[edge[0]] = d[j]+edge[1]
                    if i >= N-1 and L[edge[0]] == 1:
                        return -1
    return d

ans = BellmanFord(E, N, 0)
if ans == -1:
    print(ans)
else:
    print(max(-ans[-1], 0))