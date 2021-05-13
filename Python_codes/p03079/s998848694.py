import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    a, b, c = list(map(int, readline().split()))
    print("Yes" if a == b == c else "No")


if __name__ == '__main__':
    solve()
