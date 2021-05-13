from collections import deque

N, M = map(int, input().split())
Edge = [[] for _ in range(N)]
Num = [0] * N
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    Edge[x].append(y)
    Num[y] += 1
Q = deque()
for i, n in enumerate(Num):
    if n == 0:
        Q.append(i)

DP = [0] * N
ans = 0
while Q:
    now = Q.pop()
    for nex in Edge[now]:
        DP[nex] = max(DP[nex], DP[now] + 1)
        Num[nex] -= 1
        if not Num[nex]:
            Q.append(nex)
print(max(DP))

