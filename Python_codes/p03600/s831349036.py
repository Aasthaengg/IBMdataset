from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
INF = 1 << 60


def input():
    return stdin.readline().strip()


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if any(A[i][j] > A[i][k] + A[k][j] for k in range(N) if k != i and k != j):
                print(-1)
                return
            if all(A[i][j] < A[i][k] + A[k][j] for k in range(N) if k != i and k != j):
                ans += A[i][j]

    print(ans)

    return


if __name__ == '__main__':
    main()
