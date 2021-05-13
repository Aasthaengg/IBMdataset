import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    a = list(map(int, input().rstrip('\n').split()))
    for i in range(n):
        a[i] -= i + 1
    a.sort()
    t = a[n // 2]
    mt = 0
    for v in a:
        mt += abs(t - v)
    print(mt)


if __name__ == '__main__':
    solve()
