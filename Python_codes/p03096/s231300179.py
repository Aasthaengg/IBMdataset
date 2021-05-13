def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    mod = 10 ** 9 + 7
    N = int(input())

    dp = [1] * (N + 1)
    dp[0] = 1
    D = {}
    pre = -1
    for n in range(N):
        c = int(input())
        dp[n + 1] = dp[n]
        if pre == c:
            dp[n] = 0
            continue
        r = D.setdefault(c, 0)
        dp[n + 1] = (dp[n + 1] + r) % mod
        D[c] = r + dp[n]
        pre = c
    print(dp[-1])


if __name__ == "__main__":
    main()
