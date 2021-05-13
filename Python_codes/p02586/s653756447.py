def main():
    R, C, K = list(map(int, input().split()))
    # dp[r][c][n]: r行目でn個のアイテムを拾う場合の(r, c)でのアイテムの価値の合計の最大
    dp_0 = [[0 for _ in range(C)] for _ in range(R)]
    dp_1 = [[0 for _ in range(C)] for _ in range(R)]
    dp_2 = [[0 for _ in range(C)] for _ in range(R)]
    dp_3 = [[0 for _ in range(C)] for _ in range(R)]
    V = [[0 for _ in range(C)] for _ in range(R)]
    for _ in range(K):
        r, c, v = list(map(int, input().split()))
        V[r - 1][c - 1] = v
    dp_1[0][0] = V[0][0]
    for r in range(R):
        for c in range(C):
            if r == c == 0:
                continue
            v_rc = V[r][c]
            max_dp_before_row = 0 if r == 0 else max(dp_0[r - 1][c], dp_1[r - 1][c], dp_2[r - 1][c], dp_3[r - 1][c])
            # dp[r][c][0]
            v1 = 0 if c == 0 else dp_0[r][c - 1]
            dp_0[r][c] = max(v1, max_dp_before_row)
            # dp[r][c][1]
            v1 = 0 if c == 0 else max(dp_1[r][c - 1], dp_0[r][c - 1] + v_rc)
            v2 = 0 if r == 0 else (max_dp_before_row + v_rc)
            dp_1[r][c] = max(v1, v2)
            # dp[r][c][2], dp[r][c][3]
            dp_2[r][c] = 0 if c == 0 else max(dp_2[r][c - 1], dp_1[r][c - 1] + v_rc)
            dp_3[r][c] = 0 if c == 0 else max(dp_3[r][c - 1], dp_2[r][c - 1] + v_rc)
    print(max(dp_0[R-1][C-1], dp_1[R-1][C-1], dp_2[R-1][C-1], dp_3[R-1][C-1]))


if __name__ == '__main__':
    main()
