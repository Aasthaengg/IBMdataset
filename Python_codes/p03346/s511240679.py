# AGC024B - Backfront
def main():
    N, *P = map(int, open(0).read().split())
    # dp[i] := length of a monotonically increasing subsequence which i comes at the end
    dp = [0] * (N + 1)
    for i in P:
        dp[i] = dp[i - 1] + 1
    ans = N - max(dp)
    print(ans)


if __name__ == "__main__":
    main()