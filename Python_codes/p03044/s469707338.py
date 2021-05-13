import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N = int(input())
edge = [[] for _ in range(N)]

for i in range(N-1):
    u,v,w = map(int, input().split())
    u, v, w = u - 1, v - 1, w % 2
    edge[u].append((v,w))
    edge[v].append((u,w))

ans = [-1] * N
queue = deque([0])

#頂点1を0色に塗る
ans[0] = 0

while queue:
    a = queue.popleft()
    for ve in edge[a]:
        if ans[ve[0]] == -1:
            if ve[1] == 0:
                ans[ve[0]] = ans[a]
            else:
                ans[ve[0]] = (ans[a]+1) % 2
            queue.append(ve[0])

for a in ans:
    print(a)