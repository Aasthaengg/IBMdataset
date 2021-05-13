from collections import defaultdict, deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M, P = map(int, input().split())
d = defaultdict(list)
e = defaultdict(list)
cd = defaultdict(list)
l = []

for _ in range(M):
    a, b, c = map(int, input().split())
    cd[a].append((b, P-c))
    d[a].append(b)
    e[b].append(a)

def check_visited(d, start):
    visited = [False]*(N+1)
    visited[start] = True
    q = deque([start])
    while q:
        s = q.popleft()
        for t in d[s]:
            if visited[t]:continue
            visited[t] = True
            q.append(t)
    
    s = set()
    for i in range(1, N+1):
        if visited[i]:
            s.add(i)
    return s

def shortest_path(s):
    INF = 10**18
    dist = [float("inf")]*(N+1)
    dist[s] = 0

    for i in range(N):
        for a, b, c in l:
            if dist[b]>dist[a]+c:
                dist[b] = dist[a]+c
                if i==N-1:
                    return dist, True
    return dist, False

add_l = check_visited(d, 1)&check_visited(e, N)
for a in add_l:
    for b, c in cd[a]:
        l.append((a, b, c))
d1, neg = shortest_path(1)
if neg:
    print(-1)
elif d1[N]<0:
    print(-d1[N])
else:
    print(0)
