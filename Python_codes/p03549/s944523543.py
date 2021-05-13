import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, readline().split()))
    print(sum([100 * (n - m) + 1900 * m for _ in range(2 ** m)]))


if __name__ == '__main__':
    solve()
