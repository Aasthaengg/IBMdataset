import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, readline().split()))
    n += 1 if n % 2 != 0 else 0
    print("YES" if n // 2 >= k else "NO")


if __name__ == '__main__':
    solve()
