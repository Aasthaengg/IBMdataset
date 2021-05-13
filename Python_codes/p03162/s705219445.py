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


def main():

    N = in_n()
    abc = in_nl2(N)

    dp = [[0 for _ in range(N)] for _ in range(3)]

    a, b, c = abc[0]
    dp[0][0] = a
    dp[1][0] = b
    dp[2][0] = c

    for i in range(N - 1):
        a, b, c = abc[i + 1]
        dp[0][i + 1] = max(dp[1][i] + a, dp[2][i] + a)
        dp[1][i + 1] = max(dp[0][i] + b, dp[2][i] + b)
        dp[2][i + 1] = max(dp[0][i] + c, dp[1][i] + c)

    print(max(dp[0][-1], dp[1][-1], dp[2][-1]))


if __name__ == '__main__':
    main()
