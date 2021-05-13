import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    s, w = list(map(int, readline().split()))
    print("unsafe" if s <= w else "safe")


if __name__ == '__main__':
    solve()
