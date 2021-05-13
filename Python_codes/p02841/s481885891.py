import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    m, d = list(map(int, input().rstrip('\n').split()))
    m, d = list(map(int, input().rstrip('\n').split()))
    print(1 if d == 1 else 0)


if __name__ == '__main__':
    solve()
