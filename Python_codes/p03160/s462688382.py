def main():
    N = int(input())
    h = list(map(int, input().split()))

    dp = [0] * N
    dp[1] = abs(h[0] - h[1])
    for i in range(2, N):
        dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

    print(dp[-1])
    return


if __name__ == '__main__':
    main()
