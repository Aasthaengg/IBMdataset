import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def isqrt(n):
    if n > 0:
        x = 1 << (n.bit_length() + 1) // 2
        y = (x + n // x) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x
    elif n == 0:
        return 0
    else:
        raise ValueError("isqrt() argument must be nonnegative")


def main():
    N = int(readline())
    n = (isqrt(8 * N + 1) - 1) // 2
    if N != n * (n + 1) // 2:
        print('No')
        return

    it = iter(range(1, N + 1))
    G = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            G[i][j] = G[j][i] = next(it)

    print('Yes')
    print(n + 1)
    for row in G:
        print(n, end=' ')
        print(*row)
    print(n, end=' ')
    print(*(G[i][i] for i in range(n)))
    return


if __name__ == '__main__':
    main()
