import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, readline().split()))
    if k == 1:
        print(0)
    elif n < k:
        print(1)
    else:
        print(n - k)


if __name__ == '__main__':
    solve()
