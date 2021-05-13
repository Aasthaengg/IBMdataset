def main():
    INF = 10 ** 10
    N, M = list(map(int, input().split(' ')))
    key_list = list()
    for _ in range(M):
        A, _ = list(map(int, input().split(' ')))
        C = list(map(lambda x: int(x) - 1, input().split(' ')))
        boxes = 0
        for c in C:
            boxes |= (1 << c)
        key_list.append((A, boxes))
    # bit DP
    # dp[m][S]: m個目までのカギでSに含まれる宝箱を開けるための最小費用
    dp = [[INF for _ in range(1 << N)] for _ in range(M + 1)]
    for m in range(M + 1):
        dp[m][0] = 0
    for m in range(1, M + 1):
        cost, box = key_list[m - 1]
        for S in range(1 << N):
            dp[m][S] = min(dp[m][S], dp[m - 1][S])
            if box | S != S:
                dp[m][box | S] = min(dp[m][box | S], dp[m - 1][S] + cost)
    ans = dp[M][(1 << N) - 1]
    if ans >= INF:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
