import sys
from collections import deque

N, M = map(int, input().split())

Edge = [[] for _ in range(3*N)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    Edge[u].append(N + v)
    Edge[N + u].append(2*N + v)
    Edge[2*N + u].append(v)

S, T = map(int, input().split())
S -= 1
T -= 1

Q = deque([S])
visited = set([S])
dist = [-3]*(3*N)
dist[S] = 0


while Q:
    vn = Q.pop()
    for vf in Edge[vn]:
        if vf in visited:
            continue
        visited.add(vf)
        dist[vf] = dist[vn] + 1
        Q.appendleft(vf)

print(dist[T]//3)    
