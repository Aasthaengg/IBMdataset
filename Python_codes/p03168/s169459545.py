def main():
    N = int(input())
    P = [float(v) for v in input().split()]

    dp = [0] * (N + 1)
    dp[0] = 1

    for i, p in enumerate(P):
        p2 = 1 - p
        for j in range(i + 1, -1, -1):
            if j >= 0:
                dp[j] = dp[j] * p2 + dp[j - 1] * p
            else:
                dp[j] = dp[j] * p2

    ldp = len(dp)
    s = ldp - len(dp) // 2

    print(sum(dp[s:]))

main()
