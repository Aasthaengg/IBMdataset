import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    a = list(map(int, readline().split()))
    for i in range(n):
        a[i] -= i + 1
    a.sort()
    t = 0
    for v in a:
        t += abs(a[n // 2] - v)
    print(t)


if __name__ == '__main__':
    solve()
