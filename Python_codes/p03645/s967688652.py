from collections import deque 


N, M = map(int, input().split())
to = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    to[a].append(b)
    to[b].append(a)
    
que = deque()
que.append(0)
dist = [-1] * N
dist[0] = 0

while que:
    island = que.popleft()
    for nxt in to[island]:
        if dist[nxt] != -1:
            continue
        que.append(nxt)
        dist[nxt] = dist[island] + 1
        
print('POSSIBLE' if dist[N - 1] == 2 else 'IMPOSSIBLE')