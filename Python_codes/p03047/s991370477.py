import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, readline().split()))
    print(n - k + 1)


if __name__ == '__main__':
    solve()
