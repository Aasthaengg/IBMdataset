import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    A, B = map(int, input().split())

    if (A + B) % 2 == 0:
        ans = (A + B) // 2
    else:
        ans = 'IMPOSSIBLE'

    print(ans)


if __name__ == '__main__':
    solve()
