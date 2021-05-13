from collections import defaultdict, deque

MOD = int(1e9+7)
N, K = map(int, input().split())
# def dfs(s, E):
E = defaultdict(list)
for i in range(N-1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)
visited = [False] * N
q = deque()
q.append(1)
visited[0] = True
ans = K
while q:
    now = q.pop()
    if now == 1:
        available = K-1
    else:
        available = K-2
    for nxt in E[now]:
        if not visited[nxt-1]:
            if available <= 0:
                print(0)
                exit()
            ans = (ans * available) % MOD
            available -= 1
            q.append(nxt)
            visited[nxt - 1] = True
print(ans)