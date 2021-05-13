from collections import deque

N, M = map(int, input().split())

g = tuple(set() for _ in range(N))
for _ in range(M):
    a, b = (int(x) - 1 for x in input().split())
    g[a].add(b)
    g[b].add(a)

print('Yes')

ret = [-1] * N
ret[0] = 0

dq = deque()
dq.append(0)

while dq:
    v = dq.popleft()
    for u in g[v]:
        if ~ret[u]: continue
        ret[u] = v
        dq.append(u)

print(*(x + 1 for x in ret[1:]), sep='\n')
