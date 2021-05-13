import sys

input = lambda: sys.stdin.readline().rstrip()

INF = 10 ** 5 + 1


def solve():
    N = int(input())
    B = list(map(int, input().split()))
    A = [INF] * N

    for i in range(N - 1):
        A[i] = min(A[i], B[i])
        A[i + 1] = min(A[i + 1], B[i])

    print(sum(A))


if __name__ == '__main__':
    solve()
