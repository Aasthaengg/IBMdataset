import collections


def bellman_ford(es, n, start):
    infinity = float("inf")
    m = len(es)

    d = [infinity] * (n + 1)
    d[start] = 0

    for _ in range(m):
        updated = False

        for u, v, w in es:
            if d[u] == infinity: continue

            dd = d[u] + w

            if dd < d[v]:
                d[v] = dd
                updated = True

        if not updated: break

    for u, v, w in es:
        if d[u] < infinity and d[u] + w < d[v]:
            return None, True

    return d, False


N, M, P = [int(e) for e in input().split()]

Es = [None] * M

for i in range(M):
    a, b, c = ([int(e) for e in input().split()])
    Es[i] = (a - 1, b - 1, P - c)

q = collections.deque()
q.append(N - 1)

valid = [False] * N
valid[N - 1] = True

while 0 < len(q):
    cur = q.popleft()

    for u, v, _ in Es:
        if cur == v and not valid[u]:
            valid[u] = True
            q.append(u)

es_tmp = []
for e in Es:
    if valid[e[0]] and valid[e[1]]:
        es_tmp.append(e)

Es = es_tmp

distances, le = bellman_ford(Es, N - 1, 0)

if le:
    print(-1)
else:
    print(max(-distances[-1], 0))
