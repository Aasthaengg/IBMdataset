import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    x, a, b = list(map(int, readline().split()))
    if b - a <= 0:
        print("delicious")
    elif 0 < b - a <= x:
        print("safe")
    else:
        print("dangerous")


if __name__ == '__main__':
    solve()
