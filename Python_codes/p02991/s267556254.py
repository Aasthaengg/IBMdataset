from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
S, T = map(int, input().split())

path = [[-1] * 3 for _ in range(N + 1)]
path[S][0] = 0
node = deque([(S, 0)])
while node:
    s, d = node.popleft()
    dist = path[s][d]

    d = (d+1) % 3
    for t in edge[s]:
        if path[t][d] != -1:
            continue
        path[t][d] = dist + 1
        node.append((t, d))


ans = path[T][0]//3
print(ans)
