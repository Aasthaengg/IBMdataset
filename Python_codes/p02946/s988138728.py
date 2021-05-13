import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    K, X = map(int, input().split())
    low = max(-1000000, X - K + 1)
    up = min(1000000, X + K - 1)

    ans = []
    for i in range(low, up + 1):
        ans.append(str(i))
    print(' '.join(ans))


if __name__ == '__main__':
    solve()
