import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, a, b = list(map(int, readline().split()))
    if (abs(a - b) - 1) % 2 != 0:
        print("Alice")
    else:
        print("Borys")


if __name__ == '__main__':
    solve()
