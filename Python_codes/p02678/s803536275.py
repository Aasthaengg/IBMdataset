N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(lambda x: int(x)-1, input().split())
    adj[A].append(B)
    adj[B].append(A)

from collections import deque

queue = deque([0])
visit = [-1] * N
visit[0] = 1

while queue:
    now = queue.popleft()
    for u in adj[now]:
        if visit[u] < 0:
            queue.append(u)
            visit[u] = visit[now] + 1

print('Yes')
for i in range(1,N):
    for u in adj[i]:
        if visit[u] == visit[i]-1:
            print(u+1)
            break