import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    flg = [[True] * n for _ in range(n)]

    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if i == j or j == k:
                    continue
                if A[i][j] > A[i][k] + A[k][j]:
                    print(-1)
                    exit()
                elif A[i][j] == A[i][k] + A[k][j]:
                    flg[i][j] = False

    res = 0
    for i in range(n):
        for j in range(n):
            if flg[i][j]:
                res += A[i][j]

    print(res // 2)


if __name__ == '__main__':
    resolve()
