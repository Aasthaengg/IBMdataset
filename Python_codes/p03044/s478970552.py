N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    A,B,C = list(map(int,input().split()))
    G[A-1].append([C,B-1]) #重み、向かう先の順番
    G[B-1].append([C,A-1])

from collections import deque
dist = [None]*N
que = deque([0])
dist[0] = 0
while que:
    v = que.popleft()
    d = dist[v]
    for c,w in G[v]:
        if dist[w] is not None:
            continue
        dist[w] = d + c
        que.append(w)
for i in range(N):
    print(dist[i]%2)