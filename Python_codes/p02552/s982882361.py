import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    x = int(readline())
    print(0 if x == 1 else 1)


if __name__ == '__main__':
    solve()
