import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    print((1000 - n % 1000) % 1000)


if __name__ == '__main__':
    solve()
