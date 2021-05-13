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
            required = True
            for k in range(N):
                if k == i or k == j:
                    continue
                if A[i][j] > A[i][k] + A[k][j]:
                    print(-1)
                    return
                if A[i][j] == A[i][k] + A[k][j]:
                    required = False
                    break
            if required:
                ans += A[i][j]

    print(ans)

    return


if __name__ == '__main__':
    main()
