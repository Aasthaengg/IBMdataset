import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    B = [0] * n
    for i in range(n):
        B[0] += A[i] if i % 2 == 0 else -A[i]

    for j in range(1, n):
        B[j] = 2 * A[j - 1] - B[j - 1]

    print(*B)


if __name__ == '__main__':
    resolve()
