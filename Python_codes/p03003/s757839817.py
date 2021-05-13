def main():
    MOD = 10 ** 9 + 7
    N, M = list(map(int, input().split(' ')))
    S = list(map(int, input().split(' ')))
    T = list(map(int, input().split(' ')))
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    sdp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for n, s in enumerate(S):
        for m, t in enumerate(T):
            sdp_val = sdp[n][m]
            new_dp_val = (sdp_val + 1) if s == t else 0
            dp[n + 1][m + 1] = new_dp_val % MOD
            sdp[n + 1][m + 1] = (sdp[n][m + 1] + sdp[n + 1][m] - sdp_val + new_dp_val) % MOD
    print((sdp[N][M] + 1) % MOD)  # 1: an empty sequence


if __name__ == '__main__':
    main()