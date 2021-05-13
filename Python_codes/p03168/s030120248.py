import sys
from copy import copy

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(float, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    N = in_n()
    p = in_nl()

    dp = [0] * (N + 1)
    dp[0] = 1 - p[0]
    dp[1] = p[0]

    for i in range(1, N):
        next_dp = copy(dp)
        for j in range(i + 2):
            next_dp[j] = dp[j] * (1 - p[i])
            if j - 1 >= 0:
                next_dp[j] += dp[j - 1] * p[i]
        dp = next_dp

    print(sum(dp[N // 2 + 1:]))


if __name__ == '__main__':
    main()
