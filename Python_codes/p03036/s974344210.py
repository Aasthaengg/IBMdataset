import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    r, d, x = map(int, input().split())
    xl = [0] * 11
    xl[0] = x
    for i in range(10):
        xl[i + 1] = r * xl[i] - d

    for i in range(1, 11):
        print(xl[i])


if __name__ == '__main__':
    solve()
