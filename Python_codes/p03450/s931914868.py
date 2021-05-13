from collections import deque

N, M = map(int, input().split())
G = [deque() for i in range(N+1)]
x = [0] * (N+1)
visited = [True] * (N+1)

for i in range(M):
    L, R, D = map(int, input().split())
    G[L].append((R, D))
    G[R].append((L, -D))
    visited[L] = False
    visited[R] = False
    
for i in range(1, N+1):
    if not visited[i]:
        q = G[i]
        visited[i] = True
        
        while q:
            u, d = q.pop()
            
            for v, d_ in G[u]:
                if visited[v]:
                    if x[v] != d+d_:
                        print('No')
                        exit()
                else:
                    visited[v] = True
                    x[v] = d+d_
                    q.append((v, d+d_))
print('Yes')      