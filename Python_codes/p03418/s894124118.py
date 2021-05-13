import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, k = list(map(int, readline().split()))
    cnt = 0
    for i in range(1, n + 1):
        if i > k:
            cnt += int((n - n % i) / i * (i - k) + max(0, n % i - max(1, k) + 1))
    print(cnt)


if __name__ == '__main__':
    solve()
