def main():
    N = int(input())
    dp = [[[[0
            for c3 in range(4)]
            for c2 in range(4)]
            for c1 in range(4)]
            for L  in range(N+1)]
    dp[0][3][3][3] = 1
    for L in range(1, N+1):
        for c3 in range(4):
            for c2 in range(4):
                for c1 in range(4):
                    for c0 in range(4):
                        if ((c2 == 0 and c1 == 2 and c0 == 1) or
                            (c2 == 2 and c1 == 0 and c0 == 1) or
                            (c2 == 0 and c1 == 1 and c0 == 2) or
                            (c3 == 0 and c2 == 2 and c0 == 1) or
                            (c3 == 0 and c1 == 2 and c0 == 1)):
                            continue
                        dp[L][c0][c1][c2] += dp[L-1][c1][c2][c3]
                        dp[L][c0][c1][c2] %= 10**9 + 7
    ans = 0
    for c3 in range(4):
        for c2 in range(4):
            for c1 in range(4):
                ans += dp[N][c1][c2][c3]
                ans %= 10**9 + 7
    print(ans)

if __name__ == "__main__":
    main()
