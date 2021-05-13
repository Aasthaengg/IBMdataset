from collections import Counter

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
grid = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]

group = [Counter() for _ in range(3)]
for i in range(N):
    for j in range(N):
        group[(i + j) % 3][grid[i][j]] += 1

ans = float('inf')
for c0 in range(C):
    for c1 in range(C):
        if c0 == c1:
            continue
        for c2 in range(C):
            if c2 == c0 or c2 == c1:
                continue
            cnt = 0
            color = [c0, c1, c2]
            for G, nc in zip(group, color):
                for c in list(G.keys()):
                    cnt += G[c] * D[c][nc]
            ans = min(ans, cnt)

print(ans)
