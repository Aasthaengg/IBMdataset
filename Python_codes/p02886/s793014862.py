import sys
import itertools
input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    d = list(map(int, input().split()))

    ruiseki = list(itertools.accumulate(d))
    ans = 0
    for i in range(N - 1):
        ans += d[i] * (ruiseki[N - 1] - ruiseki[i])

    print(ans)


if __name__ == '__main__':
    solve()
