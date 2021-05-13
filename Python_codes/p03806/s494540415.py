def main():
    N, MA, MB = list(map(int, input().split()))
    chemicals = [list(map(int, input().split())) for _ in range(N)]
    INF_COST = 1 + sum([chemical[2] for chemical in chemicals])
    MAX_A, MAX_B = 400, 400
    # dp[a][b]: 物質Aをaグラム、物質Bをbグラム入手するのに必要な最小コスト
    #           状態数は400 * 400 = 160000
    #           薬品の個数は40個
    #           → 更新ステップ数は 160000 * 40 = 6400000 = 6.4 * (10**6)
    dp = [[INF_COST for _ in range(1 + MAX_B)] for _ in range(1 + MAX_A)]
    dp[0][0] = 0
    for chemical in chemicals:
        da, db, dc = chemical
        for a in range(MAX_A, -1, -1):
            if a + da > MAX_A:
                continue
            for b in range(MAX_B, -1, -1):
                if b + db > MAX_B:
                    continue
                dp[a + da][b + db] = min(dp[a + da][b + db], dc + dp[a][b])
    ans = INF_COST
    scale = 1
    while scale * MA <= MAX_A and scale * MB <= MAX_B:
        ans = min(ans, dp[scale * MA][scale * MB])
        scale += 1
    if ans == INF_COST:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
