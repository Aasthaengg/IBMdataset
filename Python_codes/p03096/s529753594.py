from collections import defaultdict

MOD = int(1e9) + 7


def main():
    N = int(input())
    C = [int(input()) for _ in range(N)]
    dp = [1] * (N+1)
    last = defaultdict(lambda: -1)
    for i in range(N):
        c = C[i]
        if last[c] != -1 and last[c] != i-1:
            dp[i+1] = (dp[i] + dp[last[c]+1]) % MOD
        else:
            dp[i+1] = dp[i]
        last[c] = i
    print(dp[N])


if __name__ == "__main__":
    main()
