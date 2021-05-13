def mod(x):
    return int(x % (1e+9 + 7))


def combination_dp(s):
    if s < 3:
        return 0
    dp = []
    dp.append(1)
    for i in range(1, s + 1):
        if i < 3:
            dp.append(0)
        else:
            start = 0
            end = i - 3 + 1
            dp.append(mod(sum(dp[start: end])))
    return dp[-1]


if __name__ == '__main__':
    S = int(input())
    print(combination_dp(S))
