import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N, D = map(int, input().split())
    if N < (D * 2 + 1):
        ans = 1
    else:
        q, r = divmod(N, D * 2 + 1)
        ans = q + 1 if r > 0 else q
    print(ans)


if __name__ == '__main__':
    solve()
