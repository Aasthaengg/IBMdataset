import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    cnt = 0
    for i in range(1, n // 2 if n % 2 == 0 else n // 2 + 1):
        if n - i <= n:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    solve()
