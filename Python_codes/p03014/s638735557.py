def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    L = [[0] * W for _ in range(H)]
    R = [[0] * W for _ in range(H)]
    D = [[0] * W for _ in range(H)]
    U = [[0] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if grid[h][w] == '#':
                continue
            if w == 0:
                L[h][w] = 1
            else:
                L[h][w] = L[h][w-1] + 1
            if h == 0:
                U[h][w] = 1
            else:
                U[h][w] = U[h-1][w] + 1
    for h in range(H - 1, -1, -1):
        for w in range(W - 1, -1, -1):
            if grid[h][w] == '#':
                continue
            if w == W - 1:
                R[h][w] = 1
            else:
                R[h][w] = R[h][w + 1] + 1
            if h == H - 1:
                D[h][w] = 1
            else:
                D[h][w] = D[h + 1][w] + 1
    ans = 0
    for h in range(H):
        for w in range(W):
            ans = max(ans, L[h][w] + R[h][w] + U[h][w] + D[h][w] - 3)
    print(ans)


if __name__ == '__main__':
    main()