from collections import defaultdict, deque

N, M = map(int, input().split())
G = defaultdict(list)
V = defaultdict(int)

for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    G[x].append(y)
    V[y] += 1

q = deque(v for v in range(N) if V[v] == 0)

dp = [0]*(N)
while q:
    From = q.popleft()
    for to in G[From]:
        dp[to] = max(dp[From]+1, dp[to])
        V[to] -= 1
        if V[to] == 0:
            q.append(to)
print(max(dp))