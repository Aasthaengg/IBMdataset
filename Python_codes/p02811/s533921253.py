import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    K, X = map(int, input().split())

    if 500 * K >= X:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
