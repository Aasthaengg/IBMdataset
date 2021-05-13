# AGC024B - Backfront
def main():
    N, *P = map(int, open(0))
    dp = [0] * (N + 1)
    for i in P:
        dp[i] = dp[i - 1] + 1
    ans = N - max(dp)
    print(ans)


if __name__ == "__main__":
    main()