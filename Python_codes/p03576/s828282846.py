import sys
from itertools import accumulate
def input(): return sys.stdin.readline().strip()

def main():
    N, K = map(int, input().split())
    points = []
    X = set()
    Y = set()
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
        X.add(x)
        Y.add(y)
    X = list(X)
    Y = list(Y)
    X.sort()
    Y.sort()

    mapX = {} # mapX[x] = (点のx座標が小さい方から何番目か)
    mapY = {} # mapY[y] = (点のy座標が小さい方から何番目か)
    for i, x in enumerate(X): mapX[x] = i + 1
    for i, y in enumerate(Y): mapY[y] = i + 1

    # 圧縮後の座標平面に対してグリッドを張るので、そのサイズを求めておく
    h, w = len(mapX), len(mapY)
    grid = [[0] * (w + 1) for _ in range(h + 1)]
    for x, y in points:
        grid[mapY[y]][mapX[x]] = 1
    sum_grid = [list(accumulate(grid[y])) for y in range(h + 1)]
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            sum_grid[y][x] += sum_grid[y - 1][x]

    ans = 10**20
    for sx in range(1, w + 1):
        for sy in range(1, h + 1):
            for ex in range(sx, w + 1):
                for ey in range(sy, h + 1):
                    cnt = sum_grid[ey][ex] - sum_grid[ey][sx-1] - sum_grid[sy-1][ex] + sum_grid[sy-1][sx-1]
                    if cnt < K: continue
                    area = (X[ex - 1] - X[sx - 1]) * (Y[ey - 1] - Y[sy - 1])
                    ans = min(ans, area)
    print(ans)


if __name__ == "__main__":
    main()
