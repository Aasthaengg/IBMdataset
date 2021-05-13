from collections import deque

n = int(input())
A = [[int(i) for i in input().split()] for j in range(n - 1)]
C = [int(i) for i in input().split()]
C.sort(reverse=True)

E = [[] for i in range(n + 1)]
V = [0] * (n + 1)

for a, b in A:
    E[a].append(b)
    E[b].append(a)

t = 0
ma = 0

for i, e in enumerate(E):
    if len(e) > ma:
        t = i
        ma = len(e)

Q = deque()
Q.append((t, 0))
i = 0
visited = [False] * (n + 1)
ans = 0

while Q:
    v, c = Q.popleft()
    if visited[v]:
        continue
    visited[v] = True
    V[v] = C[i]
    ans += min(c, C[i])
    for e in E[v]:
        Q.append((e, C[i]))
    i += 1

print(ans)
print(*V[1:])