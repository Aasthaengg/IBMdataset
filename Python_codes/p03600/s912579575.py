def warshall_floyd(e, n):
    d = [[e[j][i] for i in range(n)] for j in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    # [print(i) for i in d]
    return d

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
dgrid = warshall_floyd(grid, n)

ans = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] != dgrid[i][j]:
            print(-1)
            exit()

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i:
              continue
            if grid[i][k] + grid[k][j] == grid[i][j]:
                dgrid[i][j] = 0

ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans += dgrid[i][j]
print(int(ans))
