import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M = map(int, readline().split())
    S = list(map(int, readline().split()))
    T = list(map(int, readline().split()))

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    sdp = [[0] * (M + 2) for _ in range(N + 2)]

    dp[0][0] = 1
    for i in range(N + 1):
        sdp[i][0] = 1
    for j in range(M + 1):
        sdp[0][j] = 1

    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                dp[i + 1][j + 1] = sdp[i][j]
            sdp[i + 1][j + 1] = (sdp[i][j + 1] + sdp[i + 1][j] - sdp[i][j] + dp[i + 1][j + 1]) % MOD

    print(sdp[N][M])
    return


if __name__ == '__main__':
    main()
