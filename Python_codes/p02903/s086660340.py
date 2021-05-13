def main():
    H, W, A, B = map(int, input().split())

    g = [[0] * W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            g[r][c] = int((c < A) ^ (r >= B))

    for row in g:
        print(*row, sep='')


if __name__ == '__main__':
    main()
