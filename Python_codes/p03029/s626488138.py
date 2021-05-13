import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    A, P = map(int, input().split())
    ans = (A * 3 + P) // 2
    print(ans)


if __name__ == '__main__':
    solve()
