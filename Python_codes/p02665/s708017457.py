import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    v = [tuple() for _ in range(N + 1)]
    v[N] = (A[N], A[N])

    if A[0] != 0:
        if A[0] == 1 and N == 0:
            print(1)
            exit()
        else:
            print(-1)
            exit()
    if N == 0:
        print(1)
        exit()

    for i in range(N - 1, -1, -1):
        low, up = v[i + 1][0], v[i + 1][1]
        up = min(2 ** i, up + A[i])
        if low % 2 == 0:
            low = low // 2 + A[i]
        else:
            low = low // 2 + A[i] + 1
        v[i] = (low, up)

    # print(v)
    for i in range(N):
        low, up = v[i][0], v[i][1]
        low = max(v[i + 1][0], low - A[i])
        up = min(v[i + 1][1], (up - A[i]) * 2)
        v[i + 1] = (low, up)

    ans = 0
    for i in range(N + 1):
        if v[i][0] > v[i][1]:
            print('-1')
            exit()
        ans += v[i][1]

    # print(v)
    print(ans)


if __name__ == '__main__':
    solve()
