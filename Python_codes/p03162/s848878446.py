# 解説を見た。
def main():
    days = int(input())
    happiness = [[int(x) for x in input().split()] for _ in range(days)]

    dp = [[0] * 3 for _ in range(days)]
    # dp[i][j]=(i日目に行動jをして、i日目までに得られる幸福度の和の最大値)
    dp[0] = happiness[0]
    selection = set((0, 1, 2))
    for i in range(1, days):
        for sel in selection:
            dp[i][sel] = max(
                dp[i - 1][not_sel] for not_sel in selection - set((sel,))
            ) + happiness[i][sel]
    print(max(dp[days - 1][sel] for sel in selection))


if __name__ == '__main__':
    main()
