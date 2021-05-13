from collections import deque

def read_tuple():
    return map(int, input().split())


N, M = read_tuple()
E = [[] for i in range(N+1)]
for i in range(M):
    u, v = read_tuple()
    E[u].append(v)
S, T = read_tuple()

dst = [[-1, -1, -1] for i in range(N+1)]
dst[S][0] = 0

Q = deque([(S,0)])
while len(Q):
    v, c = Q.popleft()
    for u in E[v]:
        k = (c + 1) % 3
        if dst[u][k] == -1:
            dst[u][k] = c + 1
            Q.append((u, c + 1))

print(dst[T][0] // 3 if dst[T][0] != -1 else -1)