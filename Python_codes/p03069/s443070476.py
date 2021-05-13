def main():
    N = int(input())
    S = input()
    # ゴールのイメージ：.........###########
    # 左から何個分まで白にするかで場合分けして最小回数を探索
    black_cum_sum = [0] * N
    for i, c in enumerate(S):
        if S[i] == '#':
            black_cum_sum[i] += 1
        if i > 0:
            black_cum_sum[i] += black_cum_sum[i - 1]
    ans = N - black_cum_sum[N - 1]  # 全部黒にするケース
    for n in range(1, N + 1):
        # 白をn個連続にするケース
        # 前半は黒を白に
        c = black_cum_sum[n - 1]
        # 後半は白を黒に
        c += (N - black_cum_sum[N - 1]) - (n - black_cum_sum[n - 1])
        ans = min(ans, c)
    print(ans)


if __name__ == '__main__':
    main()