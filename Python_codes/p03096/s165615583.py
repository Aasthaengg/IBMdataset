import sys
from collections import defaultdict

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

    N = in_n()
    C = list(in_all())

    mod = 10**9 + 7

    d = defaultdict(lambda: -1)
    d[C[0]] = 0
    dp = [0] * N
    dp[0] = 1

    for i in range(1, N):
        j = d[C[i]]
        if j == -1:
            dp[i] = dp[i - 1]
        elif j == i - 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + dp[j]

        dp[i] %= mod

        d[C[i]] = i

    print(dp[-1])


if __name__ == '__main__':
    main()
