from collections import defaultdict, deque
from heapq import heappush, heappop


def bfs(V, s, t):
    q = deque([(0, s)])
    used = set()
    
    while q:
        dist, a = q.popleft()
        used.add(a)
        if a == t:
            break
        for b in V[a]:
            if b in used: continue
            q.append((dist+1, b))
    
    if a != t:
        dist = -1
    else:
        dist = -1 if dist%3 else dist//3
    return dist

def dijkstra1(V, n, source):
    # O(ElogV)

    inf = float("inf")
    dist = [inf] * (n+1)
    dist[source] = 0
    q = [(0, source)]

    while q:
        cost, u = heappop(q)
        if dist[u] < cost:
            continue
        for c, v in V[u]:
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                heappush(q, (dist[v], v))

    return dist


if __name__ == "__main__":
    V = defaultdict(list)
    N, M = map(int, input().split())
    for _ in range(M):
        u, v = map(int, input().split())
        V[u].append((1, v+(N)))
        V[u+(N)].append((1, v+(2*N)))
        V[u+(2*N)].append((1, v))

    S, T = map(int, input().split())
    dist = dijkstra1(V, 3*N, S)[T]
    print(-1 if dist==float("inf") else dist//3)