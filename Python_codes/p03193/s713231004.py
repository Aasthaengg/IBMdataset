import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, h, w = list(map(int, readline().split()))
    cnt = 0
    for i in range(n):
        a, b = list(map(int, readline().split()))
        if a >= h and b >= w:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    solve()
