LI = lambda: list(map(int, input().split()))

N, M = LI()
A = [int(input()) for _ in range(M)]

MOD = 10 ** 9 + 7


def main():
    s = set(A)
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in s:
            continue
        v = dp[i - 1]
        if i >= 2:
            v += dp[i - 2]
        dp[i] = v % MOD
    
    ans = dp[-1]
    print(ans)


if __name__ == "__main__":
    main()
