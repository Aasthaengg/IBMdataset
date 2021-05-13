def main():
    n = int(input())
    dp = [0 for _ in range(n + 1)]
    for i in range(n):
        p = int(input())
        dp[p] = dp[p - 1] + 1
    non_move = 0
    for i in range(n + 1):
        non_move = max(non_move, dp[i])
    print(n - non_move)


if __name__ == '__main__':
    main()
