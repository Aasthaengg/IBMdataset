def main():
    import sys
    input = sys.stdin.readline

    H, W, K = map(int, input().split())

    G = [[0] * W for _ in range(H)]
    for _ in range(K):
        r, c, v = map(int, input().split())
        G[r - 1][c - 1] = v

    pdp = [[0] * 4 for _ in range(W)]
    for r in range(H):
        dp = [[0] * 4 for _ in range(W)]
        left = [0] * 4
        for c in range(W):
            cell = dp[c]

            for k in range(4):
                cell[k] = left[k]

            up = max(pdp[c])
            if cell[0] < up:
                cell[0] = up

            for k in range(2, -1, -1):
                cell[k + 1] = max(
                    cell[k + 1],
                    cell[k] + G[r][c])
            left = cell
        pdp = dp

    # for k in range(4):
    #     for row in range(H):
    #         for col in range(W):
    #             print(dp[row][col][k], end=' ')
    #         print()
    #     print()

    # print(*G, sep='\n')

    ans = max(dp[-1])
    print(ans)


if __name__ == '__main__':
    main()
