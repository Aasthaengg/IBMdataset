import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]

    A = sorted(A, key=lambda x: x[1])

    INF = 10**10
    cur = -INF
    cnt = 0

    for i in range(M):
        if A[i][0] < cur:
            continue
        else:
            cur = A[i][1]
            cnt += 1
    print(cnt)


resolve()