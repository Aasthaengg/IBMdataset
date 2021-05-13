INF = 10**9 + 7


def main():
    N, K = (int(i) for i in input().split())
    H = [int(i) for i in input().split()]
    dp = [INF]*N
    dp[0] = 0
    for i in range(N):
        for k in range(1, K+1):
            if i + k >= N:
                break
            dp[i+k] = min(dp[i+k], dp[i] + abs(H[i+k] - H[i]))
    print(dp[-1])


if __name__ == '__main__':
    main()
