import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    X, A = map(int, input().split())

    if X < A:
        ans = 0
    else:
        ans = 10
    print(ans)


if __name__ == '__main__':
    solve()
