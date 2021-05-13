import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
edge = [[] for _ in range(N + 1)]
for _ in range(M):
    s, t, d = map(int, input().split())
    edge[s].append((t, d))
    edge[t].append((s, -d))

dist = [None] * (N + 1)


def isOK(v):
    node = [v]
    if dist[v] is None:
        dist[v] = 0

    while node:
        s = node.pop()
        for t, d in edge[s]:
            if dist[t] is None:
                dist[t] = dist[s] + d
                node.append(t)
            else:
                if dist[t] != dist[s] + d:
                    return False
    return True


ans = "Yes"
for i in range(1, N + 1):
    if dist[i] is not None:
        continue

    if not isOK(i):
        ans = "No"
        break
print(ans)