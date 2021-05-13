def main():
    N = int(input())
    *A, = map(int, input().split())

    dp = [0] * (N + 1)
    dp[0] = 1000

    for i, a in enumerate(A):
        dp[i + 1] = dp[i]
        for j in range(i):
            buy, rest = divmod(dp[j], A[j])
            dp[i + 1] = max(dp[i + 1], buy * a + rest)

    print(dp[-1])


if __name__ == '__main__':
    main()
