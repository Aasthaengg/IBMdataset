import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, x, t = list(map(int, readline().split()))
    print((n + x - 1) // x * t)


if __name__ == '__main__':
    solve()
