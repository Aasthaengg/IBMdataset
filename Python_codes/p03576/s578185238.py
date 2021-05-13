import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    N, K = in_nn()

    X = []
    Y = []
    for i in range(N):
        x, y = in_nn()
        X.append(x)
        Y.append(y)

    sort_x = sorted(set(X))
    sort_y = sorted(set(Y))

    nx = len(sort_x)
    ny = len(sort_y)

    total_sum = [[0 for _ in range(nx + 1)] for _ in range(ny + 1)]

    for i in range(N):
        x, y = X[i], Y[i]
        ix = sort_x.index(x)
        iy = sort_y.index(y)
        total_sum[iy + 1][ix + 1] += 1

    for y in range(ny + 1):
        for x in range(nx):
            total_sum[y][x + 1] += total_sum[y][x]

    for x in range(nx + 1):
        for y in range(ny):
            total_sum[y + 1][x] += total_sum[y][x]

    def calc_area(u, d, l, r):
        return total_sum[d][r] - total_sum[u][r] - total_sum[d][l] + total_sum[u][l]

    ans = 10**19
    for y1 in range(ny + 1):
        for y2 in range(y1 + 2, ny + 1):
            for x1 in range(nx + 1):
                for x2 in range(x1 + 2, nx + 1):
                    if calc_area(y1, y2, x1, x2) >= K:
                        area = (sort_x[x2 - 1] - sort_x[x1]) * (sort_y[y2 - 1] - sort_y[y1])
                        ans = min(ans, area)

    print(ans)


if __name__ == '__main__':
    main()
