mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())

    X = [1]
    for i in range(1, 101):
        if 6**i > N:
            break
        X.append(6**i)
    for i in range(1, 101):
        if 9**i > N:
            break
        X.append(9**i)
    dp = [N+1] * (N+1)
    dp[0] = 0
    for i in range(N):
        for x in X:
            if i+x <= N:
                dp[i+x] = min(dp[i+x], dp[i] + 1)
    print(dp[N])


if __name__ == '__main__':
    main()
