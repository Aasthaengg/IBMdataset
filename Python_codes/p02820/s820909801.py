import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K = map(int, readline().split())
    R, S, P = map(int, readline().split())
    T = readline().strip()

    T = [int(c) for c in T.translate(str.maketrans('rsp', '012'))]
    H = [R, S, P]

    dp = [[0] * 3 for _ in range(N + 1)]

    for i in range(N):
        com = T[i]
        for h in range(3):
            if i > K - 1:
                dp[i + 1][h] = max(dp[i + 1 - K][(h + 1) % 3], dp[i + 1 - K][(h + 2) % 3])
            if (h + 1) % 3 == com:
                dp[i + 1][h] += H[h]

    print(sum(max(p) for p in dp[-K:]))

    return


if __name__ == '__main__':
    main()
