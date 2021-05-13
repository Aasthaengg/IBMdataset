from collections import deque

N = int(input())

T = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    T[a - 1].append((b - 1, c))
    T[b - 1].append((a - 1, c))
Q, K = map(int, input().split())

# dfs
table = [0] * N
D = deque([K - 1])
visited = set()
while D:
    v = D.pop()
    visited.add(v)
    for x, d in T[v]:
        if x not in visited:
            table[x] = table[v] + d
            D.append(x)

for _ in range(Q):
    x, y = map(int, input().split())
    print(table[x - 1] + table[y - 1])
