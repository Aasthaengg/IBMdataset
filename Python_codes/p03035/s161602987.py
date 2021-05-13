import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    A, B = map(int, input().split())

    if A >= 13:
        ans = B
    elif 6 <= A and A <= 12:
        ans = B // 2
    else:
        ans = 0
    print(ans)


if __name__ == '__main__':
    solve()
