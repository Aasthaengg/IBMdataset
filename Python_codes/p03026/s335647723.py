import sys

sys.setrecursionlimit(10 ** 9 + 7)

N = int(input())
visited = [False] * N
edges = [[] for _ in range(N)]
AB = []
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    AB.append((a, b))
    edges[a].append(b)
    edges[b].append(a)
C = list(map(int, input().split()))
C.sort(reverse=True)
scores = [-1] * N
i = 0

def dfs(v):
    if visited[v]:
        return

    visited[v] = True
    global i
    scores[v] = C[i]
    i += 1
    for e in edges[v]:
        if visited[e]:
            continue

        dfs(e)

dfs(0)

total = 0
for a, b in AB:
    total += min(scores[a], scores[b])
print(total)
print(*scores)