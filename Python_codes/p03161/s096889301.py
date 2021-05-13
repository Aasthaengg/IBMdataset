from numba import njit


@njit
def main(N, K, h):
    dp = [10**10] * (N+1)
    dp[0] = 0

    for i in range(1, N):
        for j in range(min(i, K)):
            dp[i] = min(dp[i], dp[i-j-1]+abs(h[i]-h[i-j-1]))

    return dp[N-1]


if __name__ == "__main__":
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    print(main(N, K, h))
