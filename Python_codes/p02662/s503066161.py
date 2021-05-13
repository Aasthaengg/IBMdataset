import sys
import copy

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    N, S = in_nn()
    A = in_nl()

    dp = [0] * (S + 1)
    dp[0] = 1

    mod = 998244353
    for i in range(N):
        next_dp = [0] * (S + 1)
        for j in range(S + 1):
            next_dp[j] += dp[j] * 2
            next_dp[j] %= mod
            if j + A[i] <= S:
                next_dp[j + A[i]] += dp[j]
                next_dp[j + A[i]] %= mod

        dp = next_dp

    print(dp[S])


if __name__ == '__main__':
    main()
