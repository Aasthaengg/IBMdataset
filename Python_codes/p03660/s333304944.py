from collections import deque

N, *AB = map(int, open(0).read().split())

E = [[] for _ in range(N + 1)]
for a, b in zip(*[iter(AB)] * 2):
    E[a].append(b)
    E[b].append(a)


def get_dist(src):
    Q = deque([src])
    dist = [0] * (N + 1)
    while Q:
        v =  Q.popleft()
        for u in E[v]:
            if dist[u] == 0:
                Q.append(u)
                dist[u] = dist[v] + 1
    return dist[1:]

F = get_dist(1)
S = get_dist(N)

fennec, snuke = 0, 0
for f, s in zip(F, S):
    if f <= s:
        fennec += 1
    else:
        snuke += 1

if fennec > snuke:
    print("Fennec")
else:
    print("Snuke")
