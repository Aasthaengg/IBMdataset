import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    a, b, c, k = list(map(int, input().rstrip('\n').split()))
    print(a - b if k % 2 == 0 else b - a)


if __name__ == '__main__':
    solve()
