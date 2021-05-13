from collections import deque
import sys


def bfs(s, trail):
    q = deque()
    q.append((s, 0))
    trail[s] = 0
    while q:
        p, step = q.popleft()
        for np in edge[p]:
            nstep = step + 1
            if trail[np] > nstep:
                q.append((np, nstep))
                trail[np] = nstep


N = int(input())
edge = [[] for _ in range(N)]
for s in sys.stdin.readlines():
    a, b = map(int, s.split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)


INF = 10 ** 9
path0 = [INF] * N
pathN = [INF] * N

bfs(0, path0)
bfs(N - 1, pathN)

fennec = 0
snuke = 0
for i in range(N):
    if path0[i] <= pathN[i]:
        fennec += 1
    else:
        snuke += 1

ans = 'Fennec' if fennec > snuke else 'Snuke'
print(ans)
