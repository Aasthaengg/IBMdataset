from collections import deque, defaultdict
N, M = map(int, input().split())
adj = [[0]*(N+1) for _ in range(N+1)] #1idx
edges = [tuple(map(int, input().split())) for _ in range(M)]
bridges = []
for e in edges:
    x,y=e
    adj[x][y] = 1
    adj[y][x] = 1

for bridge in edges:
    bx, by = bridge
    adj[bx][by] = 0
    adj[by][bx] = 0
    seen = [0]*(N+1)
    def dfs(s):
        seen[s] = 1
        for nx in range(1, N+1):
            if adj[s][nx]:
                if seen[nx]:
                    continue
                dfs(nx)
    dfs(1)
    is_ok = 1
    for i in range(1, N+1):
        if not seen[i]:
            is_ok = 0
            break
    if not is_ok:
        bridges.append(bridge)
    adj[bx][by] = 1
    adj[by][bx] = 1

print(len(bridges))