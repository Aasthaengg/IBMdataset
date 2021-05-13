import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, a, b = list(map(int, readline().split()))
    print("Alice" if abs(a - b) % 2 == 0 else "Borys")


if __name__ == '__main__':
    solve()
