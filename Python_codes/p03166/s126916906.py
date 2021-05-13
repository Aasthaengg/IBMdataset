from collections import deque

N, M = map(int, input().split())

in_node = [0 for i in range(N+1)]
G = [[] for i in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    G[x].append(y)
    in_node[y] += 1

que = deque()

dp = [0 for i in range(N+1)]

for i in range(1, N+1):
    if in_node[i] == 0:
        que.append(i)

while que:
    x = que.popleft()
    for child_node in G[x]:
        dp[child_node] = max(dp[child_node], dp[x]+1)
        in_node[child_node] -= 1
        if in_node[child_node] == 0:
            que.append(child_node)

ans = max(dp)

print(ans)