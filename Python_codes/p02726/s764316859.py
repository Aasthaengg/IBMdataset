from collections import deque
N, X, Y = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
    G[i].append(i + 1)
    G[N-i-1].append(N - i - 2)
G[X-1].append(Y-1)
G[Y-1].append(X-1)

mind = [[N] * N for _ in range(N)]
todo = deque()
for s in range(N):
    todo.append((0, s))
    done = set()
    while todo:
        d, p = todo.popleft()
        mind[s][p] = min(mind[s][p], d)
        done.add(p)
        for np in G[p]:
            if not np in done:
                todo.append((d + 1, np))

counts = [0] * (N - 1)
for i in range(N - 1):
    for j in range(i + 1, N):
        counts[mind[i][j]-1] += 1
for c in counts:
    print(c)