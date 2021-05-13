import sys

N = int(sys.stdin.readline())

d = []
for _ in range(N):
    d.append(list(map(int, sys.stdin.readline().split())))

grid_min_path = [[True for _ in range(N)] for _ in range(N)]

def warshall_floyd(d, n, grid_min_path):
    changed = False
    path_length = 0
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    changed = True
                if d[i][j] == d[i][k] + d[k][j] and i != k and k != j:
                    # print(i, j, k)
                    grid_min_path[i][j] = False
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d, changed, grid_min_path

d, changed, grid_min_path = warshall_floyd(d, N, grid_min_path)
# print(grid_min_path)
if changed:
    print(-1)
else:
    length = 0
    for i in range(N):
        for j in range(i+1, N):
            if grid_min_path[i][j]:
                length += d[i][j]
    print(length)