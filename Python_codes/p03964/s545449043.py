import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    N = int(input())
    A, B = [0] * N, [0] * N

    for i in range(N):
        A[i], B[i] = map(int, input().split())

    x = 1

    for i in range(N-1):
        x = max(-(-A[i]*x // A[i+1]), -(-B[i]*x // B[i+1]))

    print(x*(A[N-1]+B[N-1]))


resolve()