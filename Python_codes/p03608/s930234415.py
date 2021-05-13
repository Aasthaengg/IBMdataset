from itertools import permutations

N, M, R = map(int, input().split())
T = list(map(int, input().split()))
grid = [[float('inf')] * N for _ in range(N)]

for i in range(N):
    grid[i][i] = 0
for i in range(M):
    A, B, C = map(int, input().split())
    A -= 1; B -= 1
    if grid[A][B] > C:
        grid[A][B] = C
        grid[B][A] = C

for k in range(N):
    for i in range(N):
        for j in range(N):
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

ans = float('inf')
for path in permutations(T):
    cnt = 0
    for i in range(R - 1):
        s = path[i] - 1
        g = path[i + 1] - 1
        cnt += grid[s][g]
    ans = min(ans, cnt)

print(ans)
