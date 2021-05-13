import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    a = list(map(int, readline().split()))
    for i in range(n):
        a[i] -= i + 1
    a.sort()
    t1 = 0
    t2 = 0
    for i in range(n):
        t1 += abs(a[i] - a[n//2])
        t2 += abs(a[i] - a[n//2 - 1])
    print(min(t1, t2))


if __name__ == '__main__':
    solve()
