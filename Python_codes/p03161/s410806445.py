def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = 0
    for i in range(1, N):
        vals = []
        for j in range(1, K+1):
            if i - j < 0:
                break
            vals.append(dp[i-j] + abs(H[i] - H[i-j]))
        dp[i] = min(vals)
    print(dp[-1])


if __name__ == '__main__':
    main()
