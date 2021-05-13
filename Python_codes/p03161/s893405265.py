import sys

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


INF = 10**18


def main():

    N, K = in_nn()
    H = in_nl()

    dp = [INF] * N
    dp[0] = 0

    for i in range(N):
        for k in range(1, K + 1):
            if i + k < N:
                dp[i + k] = min(dp[i + k], dp[i] + abs(H[i] - H[i + k]))

    print(dp[-1])


if __name__ == '__main__':
    main()
