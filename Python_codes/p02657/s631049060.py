import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    a, b = list(map(int, readline().split()))
    print(a * b)


if __name__ == '__main__':
    solve()
