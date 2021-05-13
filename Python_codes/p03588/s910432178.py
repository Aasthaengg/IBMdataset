import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    ab = [list(map(int, readline().split())) for _ in range(n)]
    ab.sort()
    print((ab[-1][0] - ab[0][0] + 1) + (ab[0][0] - 1) + (ab[-1][1]))


if __name__ == '__main__':
    solve()
