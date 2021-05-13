def solve(N, Cs):
    dp = [-1 for _ in Cs]
    latest_c = {}
    ans = 1
    d = 10 ** 9 + 7
    for i, c in enumerate(Cs):
        if c not in latest_c:
            latest_c[c] = i
            dp[i] = ans
        else:
            previous_i = latest_c[c]
            if previous_i != i - 1:
                ans += dp[previous_i]
            latest_c[c] = i
            dp[i] = ans
    return ans % d


if __name__ == "__main__":
    N = int(input())
    Cs = [int(input()) for _ in range(N)]
    print(solve(N, Cs))
