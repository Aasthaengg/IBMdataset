def main():
    INF = 10 ** 6
    H, W = list(map(int, input().split(' ')))
    A = [input() for _ in range(H)]
    d = [[INF for _ in range(W)] for _ in range(H)]
    # 距離テーブルの初期化
    for h in range(H):
        for w in range(W):
            if A[h][w] == '#':
                d[h][w] = 0
    # 黒マスまでの横方向の最短距離を出す
    for h in range(H):
        # 左から右方向へ探索
        for w in range(1, W):
            d[h][w] = min(d[h][w], 1 + d[h][w - 1])
        # 逆方向
        for w in range(W - 2, -1, -1):
            d[h][w] = min(d[h][w], 1 + d[h][w + 1])
    # 縦方向も同様に探索
    for w in range(W):
        for h in range(1, H):
            d[h][w] = min(d[h][w], 1 + d[h - 1][w])
        for h in range(H - 2, -1, -1):
            d[h][w] = min(d[h][w], 1 + d[h + 1][w])
    # 黒マスまでの最長距離が答え
    ans = 0
    for h in range(H):
        for w in range(W):
            ans = max(ans, d[h][w])
    print(ans)


if __name__ == '__main__':
    main()