from collections import deque
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    G[u - 1].append([v - 1, w])
    G[v - 1].append([u - 1, w])

Q = deque()
Q.append(0)
c = [-1] * N
c[0] = 0
while len(Q) > 0:
    q = Q.popleft()
    pc = c[q]
    for g, w in G[q]:
        if c[g] != -1:
            continue
        if w % 2 == 0:
            c[g] = pc
        else:
            c[g] = 1 - pc
        Q.append(g)

for i in c:
    print(i)