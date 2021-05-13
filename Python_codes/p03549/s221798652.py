import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, readline().split()))
    print(1900 * m * 2 ** m + 100 * (n - m) * 2 ** m)


if __name__ == '__main__':
    solve()
