def p_d():
    n, m = map(int, input().split())
    a = map(int, input().split())
    c = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    inf = 10 ** 9
    costs = {m: c[m - 1] for m in a}
    # dp(i) := ちょうど i 本のマッチ棒を使って、条件を満たす整数を作るときの最大桁数
    dp = [0]

    for i in range(1, n + 1):
        dp.append(max(
            [dp[i - c] if i - c >= 0 else -inf for c in costs.values()]
        ) + 1)

    digits = list(costs.keys())
    digits.sort(reverse=True)
    num = n
    result = []
    for _ in range(dp[n]):
        for digit in digits:
            if num >= costs[digit] and dp[num - costs[digit]] != -inf and dp[num - costs[digit]] == dp[num] - 1:
                result.append(str(digit))
                num -= costs[digit]
                break
    print("".join(result))


if __name__ == '__main__':
    p_d()
