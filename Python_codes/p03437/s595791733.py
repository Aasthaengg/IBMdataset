import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    x, y = list(map(int, readline().split()))
    if x % y != 0:
        print(x)
    else:
        print(-1)


if __name__ == '__main__':
    solve()
