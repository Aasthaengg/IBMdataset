from collections import deque
N, M, P = map(int, input().split())
G = [[] for i in range(N)]
RG = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    G[a-1].append((b-1, P-c))
    RG[b-1].append((a-1, P-c))

def chk(s, G):
    P = [0]*N
    que = deque([s])
    used = [0]*N
    used[s] = 1
    while que:
        v = que.popleft()
        P[v] = 1
        for w, c in G[v]:
            if used[w]:
                continue
            que.append(w)
            used[w] = 1
    return P
P0 = chk(0, G); P1 = chk(N-1, RG)
I = [i for i in range(N) if P0[i] == P1[i] == 1]

dist = [10**18]*N
dist[0] = 0
L = len(I)
for i in range(L+1):
    update = 0
    for v in I:
        d = dist[v]
        for w, c in G[v]:
            if d + c < dist[w]:
                dist[w] = d + c
                update = 1
    if not update:
        break
else:
    print("-1")
    exit(0)

print(max(-dist[N-1], 0))