import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    if N == 1:
        print(0)
        exit()

    ans = (N) * (N - 1) // 2
    print(ans)


if __name__ == '__main__':
    solve()
