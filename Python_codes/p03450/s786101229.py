from collections import deque
INFTY = 10**10
N,M = map(int,input().split())
ind = 2
if N==1:
    ind = 0
else:
    G = {}
    for _ in range(M):
        L,R,D = map(int,input().split())
        if L not in G:
            G[L]=[]
        G[L].append((R,D))
        if R not in G:
            G[R] = []
        G[R].append((L,-D))
    dist = [INFTY for _ in range(N+1)]
    hist = [0 for _ in range(N+1)]
    for i in G:
        ind = 2
        heap = deque([i])
        while heap:
            cur = heap.popleft()
            if hist[cur]==0:
                dist[cur] = 0
                hist[cur]=1
                ind = 0
            elif hist[cur]==1 and ind==2:
                break
            for x in G[cur]:
                v,w = x[0],x[1]
                if hist[v]==0:
                    dist[v] = dist[cur]+w
                    heap.append(v)
                    hist[v]=1
                else:
                    if dist[v]!=dist[cur]+w:
                        ind = 1
                        break
            if ind==1:break
        if ind==1:break
if ind!=1:
    print("Yes")
else:
    print("No")