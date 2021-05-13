def main():
    import sys
    my_input = sys.stdin.readline
    H, W, K = map(int, my_input().split())
    V = [[0] * W for _ in range(H)]
    for i in range(K):
        h, w, v = map(int, my_input().split())
        h, w = h - 1, w - 1
        V[h][w] = v

    # dp1 ~ 4[h][w][x] := h行w列にいて、h行からn個アイテムを拾っている時の価値の総和の最大値
    dp0 = [[0] * (W + 1) for _ in range(H + 1)]
    dp1 = [[0] * (W + 1) for _ in range(H + 1)]
    dp2 = [[0] * (W + 1) for _ in range(H + 1)]
    dp3 = [[0] * (W + 1) for _ in range(H + 1)]

    for h in range(1, H + 1):
        for w in range(1, W + 1):
            dp1[h][w] = max(
                dp1[h][w],
                dp3[h - 1][w] + V[h - 1][w - 1],
                dp1[h][w - 1],
                dp0[h][w - 1] + V[h - 1][w - 1]
            )

            dp2[h][w] = max(
                dp2[h][w],
                dp3[h - 1][w] + V[h - 1][w - 1],
                dp2[h][w - 1],
                dp1[h][w - 1] + V[h - 1][w - 1]
            )

            dp3[h][w] = max(
                dp3[h][w],
                dp3[h - 1][w] + V[h - 1][w - 1],
                dp3[h][w - 1],
                dp2[h][w - 1] + V[h - 1][w - 1]
            )

    print(dp3[-1][-1])


if __name__ == "__main__":
    main()
