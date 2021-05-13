import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, readline().split()))
    t1 = n - m
    t2 = m
    print(int((t1 * 100 + t2 * 1900) / (1 / 2) ** t2))


if __name__ == '__main__':
    solve()
