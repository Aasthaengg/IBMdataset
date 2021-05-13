import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    for i in range(N):
        ans += 1 / A[i]

    ans = 1 / ans
    print(ans)


if __name__ == '__main__':
    solve()
