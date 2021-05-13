import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    A, B, T = map(int, input().split())
    q = T // A
    print(q * B)


if __name__ == '__main__':
    solve()
