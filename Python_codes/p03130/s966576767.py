from collections import deque

def bfs():
    q = deque()
    t = 0
    x = [-1 + i for i in range(5)]
    for i in range(1, 5):
        q.append(i)
        dist = [-1] * 5
        dist[i] = 0
        while q:
            j = q.popleft()
            for i in G[j]:
                if dist[i] == -1:
                    dist[i] = dist[j] + 1
                    q.append(i)
        dist.sort()
        if x == dist:
            t = 1
            break
    return t

G = [[] for _ in range(5)]
for _ in range(3):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
print("YES" if bfs() else "NO")