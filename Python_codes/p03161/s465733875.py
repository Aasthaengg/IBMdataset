def main():
    n, k = map(int, input().split())
    nt = set(range(n))
    kt = set(range(1, k + 1))
    h = tuple(map(int, input().split()))
    INF = 10 ** 9
    dp = [INF] * n
    dp[0] = 0
    for i in nt:
        for j in kt:
            i_j = i + j
            if i_j < n:
                x = dp[i] + abs(h[i] - h[i_j])
                if dp[i_j] > x:
                    dp[i_j] = x
    print(dp[-1])


if __name__ == "__main__":
    main()