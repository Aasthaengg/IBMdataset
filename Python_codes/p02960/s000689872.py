import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    N = len(S)
    power = [0] * N
    power[0] = 1
    for i in range(N - 1):
        power[i + 1] = 10 * power[i] % 13

    S = S[::-1]

    Q = []
    const = 0
    for i, c in enumerate(S):
        if c == '?':
            Q.append(i)
        else:
            const = (const + power[i] * int(c)) % 13

    dp = [0] * 13
    dp[const] = 1

    for i in range(len(Q)):
        dp, dp_prev = [0] * 13, dp
        p = power[Q[i]]
        for j in range(10):
            for k in range(13):
                idx = (p * j + k) % 13
                dp[idx] = (dp[idx] + dp_prev[k]) % MOD

    print(dp[5])
    return


if __name__ == '__main__':
    main()
