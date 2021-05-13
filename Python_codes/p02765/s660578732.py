import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, r = list(map(int, readline().split()))
    if n >= 10:
        print(r)
    else:
        print(r + 100 * (10 - n))


if __name__ == '__main__':
    solve()
